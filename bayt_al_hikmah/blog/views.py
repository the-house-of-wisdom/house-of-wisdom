"""API endpoints for bayt_al_hikmah.blog"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from bayt_al_hikmah.blog.models import Article
from bayt_al_hikmah.blog.serializers import ArticleSerializer
from bayt_al_hikmah.mixins.views import ActionPermissionsMixin


# Create your views here.
class ArticleViewSet(ActionPermissionsMixin, ModelViewSet):
    """Base ViewSet for extension"""

    queryset = Article.objects.live()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["title", "headline", "content"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["owner"]
    action_permissions = {
        "default": [IsAuthenticated, IsAdminUser],
        "list": permission_classes,
        "retrieve": permission_classes,
    }

    def get_queryset(self):
        """Filter queryset by owner"""

        return super().get_queryset().filter(owner_id=self.request.user.id)
