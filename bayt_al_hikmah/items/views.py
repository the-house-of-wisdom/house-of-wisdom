""" API endpoints for bayt_al_hikmah.items """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.items.models import Item
from bayt_al_hikmah.items.serializers import ItemSerializer


# Create your views here.
class ItemViewSet(ModelViewSet):
    """Create, view, update and delete Module Items"""

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["title", "content"]
    ordering_fields = ["title", "created_at", "updated_at"]
    filterset_fields = ["module", "title"]


class ModuleItemsViewSet(ItemViewSet):
    """Items of a module"""

    def get_queryset(self):
        """Filter queryset by course"""

        return super().get_queryset().filter(module_id=self.kwargs["id"])

    def perform_create(self, serializer):
        """Add module to item"""

        serializer.save(module_id=self.kwargs["id"])
