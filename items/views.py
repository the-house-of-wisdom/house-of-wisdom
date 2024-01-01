""" API endpoints for learn.items """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from learn.mixins import OwnerMixin
from learn.permissions import IsOwner
from learn.items.models import Item
from learn.items.serializers import ItemSerializer


# Create your views here.
class ItemViewSet(OwnerMixin, ModelViewSet):
    """Create, view, update and delete Items"""

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "headline", "description"]
    ordering_fields = ["id", "name", "created_at", "updated_at"]
    filterset_fields = ["name"]

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes += [IsOwner]
        elif self.action in ["approve", "list"]:
            self.permission_classes += [IsAdminUser]

        return super().get_permissions()
