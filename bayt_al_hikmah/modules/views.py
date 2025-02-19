"""API endpoints for bayt_al_hikmah.modules"""

from typing import Any, List
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.modules.models import Module
from bayt_al_hikmah.modules.serializers import ModuleSerializer


# Create your views here.
class ModuleViewSet(ModelViewSet):
    """Create, view, update and delete Modules"""

    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["course"]

    def get_permissions(self) -> List[Any]:
        if self.action not in ["list", "retrieve"]:
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()
