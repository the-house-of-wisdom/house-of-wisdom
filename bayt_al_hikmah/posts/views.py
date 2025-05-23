"""API endpoints for bayt_al_hikmah.posts"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.mixins.views import ActionPermissionsMixin
from bayt_al_hikmah.posts.models import Post
from bayt_al_hikmah.posts.serializers import PostSerializer
from bayt_al_hikmah.permissions import (
    DenyAll,
    IsEnrolledOrInstructor,
    IsInstructor,
    IsOwner,
    IsPostOwner,
)
from bayt_al_hikmah.ui.mixins import UserFilterMixin


# Create your views here.
class BasePostVS(ActionPermissionsMixin, ModelViewSet):
    """Base ViewSet for extension"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsInstructor]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["user", "course"]
    action_permissions = {
        "default": [IsAuthenticated, IsInstructor, IsOwner],
        "list": permission_classes,
        "retrieve": permission_classes,
    }


class PostViewSet(UserFilterMixin, BasePostVS):
    """View, update and delete Posts"""

    action_permissions = {**BasePostVS.action_permissions, "create": [DenyAll]}


class CoursePosts(BasePostVS):
    """Create, read, update and delete Course Posts"""

    action_permissions = {
        **BasePostVS.action_permissions,
        "default": [IsAuthenticated, IsInstructor, IsPostOwner],
        "list": [IsAuthenticated, IsEnrolledOrInstructor],
        "retrieve": [IsAuthenticated, IsEnrolledOrInstructor],
    }

    def perform_create(self, serializer):
        """Add course to post automatically"""

        serializer.save(
            user_id=self.request.user.id, course_id=self.kwargs["course_id"]
        )

    def get_queryset(self):
        """Filter queryset by course"""

        return super().get_queryset().filter(course_id=self.kwargs["course_id"])
