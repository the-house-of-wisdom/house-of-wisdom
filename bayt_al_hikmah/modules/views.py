""" API endpoints for bayt_al_hikmah.modules """

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
    ordering_fields = ["title", "created_at", "updated_at"]
    filterset_fields = ["course", "id"]

    def get_queryset(self):
        """Filter queryset by user"""

        return super().get_queryset().filter(course__user=self.request.user)


class CourseModuleViewSet(ModuleViewSet):
    """Modules of a course"""

    def get_queryset(self):
        """Filter queryset by course"""

        return super().get_queryset().filter(course_id=self.kwargs["id"])

    def perform_create(self, serializer):
        """Add course to module"""

        serializer.save(course_id=self.kwargs["id"])
