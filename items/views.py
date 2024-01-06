""" API endpoints for learn.items """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from learn.mixins import OwnerMixin
from learn.modules.models import Module
from learn.permissions import IsOwner
from learn.items.models import Item
from learn.items.serializers import ItemSerializer


# Create your views here.
class ItemViewSet(OwnerMixin, ModelViewSet):
    """Create, view, update and delete Items"""

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["title", "content"]
    ordering_fields = ["id", "title", "created_at", "updated_at"]
    filterset_fields = ["module", "title"]

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes += [IsOwner]

        return super().get_permissions()


class ModuleItemsViewSet(ItemViewSet):
    """Items of a module"""

    def get_queryset(self):
        """Filter queryset by module"""

        module = Module.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(module=module)

    def perform_create(self, serializer):
        """Add an item to a module"""

        module = Module.objects.get(pk=self.kwargs["id"])
        serializer.save(module=module)
