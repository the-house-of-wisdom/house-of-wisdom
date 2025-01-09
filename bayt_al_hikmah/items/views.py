""" API endpoints for bayt_al_hikmah.items """

from typing import Any, List
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
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["lesson__module__course", "lesson__module", "lesson", "type"]

    def get_permissions(self) -> List[Any]:
        if self.action not in ["list", "retrieve"]:
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()
