""" API endpoints for learn.modules """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from learn.mixins import OwnerMixin
from learn.permissions import IsOwner
from learn.modules.models import Module
from learn.modules.serializers import ModuleSerializer


# Create your views here.
class ModuleViewSet(OwnerMixin, ModelViewSet):
    """Create, view, update and delete Modules"""

    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
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
