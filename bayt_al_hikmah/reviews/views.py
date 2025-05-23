"""API endpoints for bayt_al_hikmah.reviews"""

from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.mixins.views import ActionPermissionsMixin
from bayt_al_hikmah.reviews.models import Review
from bayt_al_hikmah.reviews.serializers import ReviewSerializer
from bayt_al_hikmah.permissions import DenyAll, IsEnrolledOrInstructor, IsOwner


# Create your views here.
class BaseReviewVS(ActionPermissionsMixin, ModelViewSet):
    """Base ViewSet for extension"""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["comment"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["user", "course", "rating", "sentiment"]
    action_permissions = {
        "default": [IsAuthenticated, IsOwner],
        "list": permission_classes,
        "retrieve": permission_classes,
    }


class ReviewViewSet(BaseReviewVS):
    """View, update and delete Reviews"""

    action_permissions = {**BaseReviewVS.action_permissions, "create": [DenyAll]}

    def get_queryset(self):
        """
        Filter queryset by user to allow users to view their reviews only and
        allow instructors to view reviews of their courses.
        """

        return (
            super()
            .get_queryset()
            .filter(
                Q(user_id=self.request.user.id)
                | Q(course__user_id=self.request.user.id)
            )
        )


class CourseReviews(BaseReviewVS):
    """Create, read, update and delete Course Reviews"""

    action_permissions = {
        **BaseReviewVS.action_permissions,
        "create": [IsAuthenticated, IsEnrolledOrInstructor],
    }

    def perform_create(self, serializer):
        """Add course to review automatically"""

        serializer.save(
            user_id=self.request.user.id, course_id=self.kwargs["course_id"]
        )

    def get_queryset(self):
        """Filter queryset by course"""

        return super().get_queryset().filter(course_id=self.kwargs["course_id"])
