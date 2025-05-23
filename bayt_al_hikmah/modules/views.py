"""API endpoints for bayt_al_hikmah.modules"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.mixins.views import ActionPermissionsMixin
from bayt_al_hikmah.modules.models import Module
from bayt_al_hikmah.modules.serializers import ModuleSerializer
from bayt_al_hikmah.permissions import (
    DenyAll,
    IsEnrolledOrInstructor,
    IsInstructor,
    IsModuleOwner,
)
from bayt_al_hikmah.ui.mixins import UserModulesMixin


# Create your views here.
class BaseModuleVS(ActionPermissionsMixin, ModelViewSet):
    """Base ViewSet for extension"""

    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated, IsInstructor]
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["course"]
    action_permissions = {"default": permission_classes}


class ModuleViewSet(UserModulesMixin, BaseModuleVS):
    """View, update and delete Modules"""

    action_permissions = {**BaseModuleVS.action_permissions, "create": [DenyAll]}


class CourseModules(BaseModuleVS):
    """Create, view, update and delete Course Modules"""

    action_permissions = {
        "default": [IsAuthenticated, IsInstructor, IsModuleOwner],
        "list": [IsAuthenticated, IsEnrolledOrInstructor],
        "retrieve": [IsAuthenticated, IsEnrolledOrInstructor],
    }

    def perform_create(self, serializer):
        """Create a module with course set automatically"""

        serializer.save(course_id=self.kwargs["course_id"])

    def get_queryset(self):
        """Filter queryset by course"""

        return super().get_queryset().filter(course_id=self.kwargs["course_id"])
