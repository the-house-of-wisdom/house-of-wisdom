""" API endpoints for bayt_al_hikmah.items """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.mixins import OwnerMixin
from bayt_al_hikmah.items.models import Item
from bayt_al_hikmah.items.serializers import ItemSerializer


# Create your views here.
class ItemViewSet(OwnerMixin, ModelViewSet):
    """Create, view, update and delete Module Items"""

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["title", "content"]
    ordering_fields = ["id", "title", "created_at", "updated_at"]
    filterset_fields = ["module", "title"]
