""" API endpoints for learn.modules """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from learn.courses.models import Course
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
    search_fields = ["title", "description"]
    ordering_fields = ["id", "title", "created_at", "updated_at"]
    filterset_fields = ["course", "title"]

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes += [IsOwner]

        return super().get_permissions()


class CourseModulesViewSet(ModuleViewSet):
    """Modules of a course"""

    def get_queryset(self):
        """Filter queryset by course"""

        course = Course.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(course=course)

    def perform_create(self, serializer):
        """Adds a module to a course"""

        course = Course.objects.get(pk=self.kwargs["id"])
        serializer.save(course=course)
