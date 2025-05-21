"""API endpoints for bayt_al_hikmah.reviews"""

from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.mixins.views import ActionPermDictMixin
from bayt_al_hikmah.reviews.models import Review
from bayt_al_hikmah.reviews.serializers import ReviewSerializer
from bayt_al_hikmah.permissions import DenyAll, IsOwner


# Create your views here.
class BaseReviewVS(ActionPermDictMixin, ModelViewSet):
    """Base ViewSet for extension"""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["comment"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["user", "course", "rating", "sentiment"]
    action_perm_dict = {
        "default": [IsAuthenticated, IsOwner],
        "list": permission_classes,
        "retrieve": permission_classes,
    }


class ReviewViewSet(BaseReviewVS):
    """View, update and delete Reviews"""

    action_perm_dict = {
        **BaseReviewVS.action_perm_dict,
        "create": [DenyAll],
    }

    def get_queryset(self):
        """Filter queryset by user"""

        return (
            super()
            .get_queryset()
            .filter(
                Q(user_id=self.request.user.pk)
                | Q(course__user_id=self.request.user.pk)
            )
        )


class CourseReviewsVS(BaseReviewVS):
    """Create, read, update and delete Course Reviews"""

    def perform_create(self, serializer):
        """Add course to review automatically"""

        serializer.save(
            user_id=self.request.user.pk, course_id=self.kwargs["course_id"]
        )

    def get_queryset(self):
        """Filter queryset by course"""

        return super().get_queryset().filter(course_id=self.kwargs["course_id"])
