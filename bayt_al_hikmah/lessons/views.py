"""API endpoints for bayt_al_hikmah.lessons"""

from typing import Any, List
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.lessons.models import Lesson
from bayt_al_hikmah.lessons.serializers import LessonSerializer
from bayt_al_hikmah.permissions import IsInstructor


# Create your views here.
class LessonViewSet(ModelViewSet):
    """Create, view, update and delete Lessons"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["module__course", "module"]

    def get_permissions(self) -> List[Any]:
        if self.action not in ["list", "retrieve"]:
            self.permission_classes = [IsAuthenticated, IsInstructor]

        return super().get_permissions()

    def get_queryset(self):
        """Filter queryset by user"""

        return (
            super()
            .get_queryset()
            .filter(
                Q(module__course__user_id=self.request.user.pk)
                | Q(module__course__students=self.request.user)
            )
        )


class ModuleLessonsViewSet(LessonViewSet):
    """Create, view, update and delete Module Lessons"""

    def perform_create(self, serializer):
        """Create a lesson with module set automatically"""

        serializer.save(module_id=self.kwargs["module_id"])

    def get_queryset(self):
        """Filter queryset by module"""

        return super().get_queryset().filter(module_id=self.kwargs["module_id"])
