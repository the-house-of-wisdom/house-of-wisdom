"""API endpoints for bayt_al_hikmah.categories"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from bayt_al_hikmah.categories.models import Category
from bayt_al_hikmah.categories.serializers import CategorySerializer
from bayt_al_hikmah.mixins.views import ActionPermissionsMixin


# Create your views here.
class CategoryViewSet(ActionPermissionsMixin, ModelViewSet):
    """Create, view, update and delete Categories"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "headline", "description"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["name"]
    action_permissions = {
        "default": [IsAuthenticated, IsAdminUser],
        "list": permission_classes,
        "retrieve": permission_classes,
    }
