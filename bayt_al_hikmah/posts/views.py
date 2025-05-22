"""API endpoints for bayt_al_hikmah.posts"""

from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.mixins.views import ActionPermDictMixin
from bayt_al_hikmah.posts.models import Post
from bayt_al_hikmah.posts.serializers import PostSerializer
from bayt_al_hikmah.permissions import DenyAll, IsOwner


# Create your views here.
class BasePostVS(ActionPermDictMixin, ModelViewSet):
    """Base ViewSet for extension"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["user", "course"]
    action_perm_dict = {
        "default": [IsAuthenticated, IsOwner],
        "list": permission_classes,
        "retrieve": permission_classes,
    }


class PostViewSet(BasePostVS):
    """View, update and delete Posts"""

    action_perm_dict = {
        **BasePostVS.action_perm_dict,
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


class CoursePostsVS(BasePostVS):
    """Create, read, update and delete Course Posts"""

    def perform_create(self, serializer):
        """Add course to post automatically"""

        serializer.save(
            user_id=self.request.user.pk, course_id=self.kwargs["course_id"]
        )

    def get_queryset(self):
        """Filter queryset by course"""

        return super().get_queryset().filter(course_id=self.kwargs["course_id"])
