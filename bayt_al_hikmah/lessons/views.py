"""API endpoints for bayt_al_hikmah.lessons"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.lessons.models import Lesson
from bayt_al_hikmah.lessons.serializers import LessonSerializer
from bayt_al_hikmah.mixins.views import ActionPermissionsMixin
from bayt_al_hikmah.permissions import (
    DenyAll,
    IsEnrolledOrInstructor,
    IsInstructor,
    IsLessonOwner,
)
from bayt_al_hikmah.ui.mixins import UserLessonsMixin


# Create your views here.
class BaseLessonVS(ActionPermissionsMixin, ModelViewSet):
    """Base ViewSet for extension"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsInstructor]
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["module__course", "module"]
    action_permissions = {
        "default": permission_classes,
        "create": permission_classes + [IsLessonOwner],
    }


class LessonViewSet(UserLessonsMixin, BaseLessonVS):
    """Create, view, update and delete Lessons"""

    action_permissions = {**BaseLessonVS.action_permissions, "create": [DenyAll]}


class ModuleLessons(BaseLessonVS):
    """Create, view, update and delete Module Lessons"""

    action_permissions = {
        "default": [IsAuthenticated, IsInstructor, IsLessonOwner],
        "list": [IsAuthenticated, IsEnrolledOrInstructor],
        "retrieve": [IsAuthenticated, IsEnrolledOrInstructor],
    }

    def perform_create(self, serializer):
        """Create a lesson with module set automatically"""

        serializer.save(module_id=self.kwargs["module_id"])

    def get_queryset(self):
        """Filter queryset by module"""

        return (
            super()
            .get_queryset()
            .filter(
                module_id=self.kwargs["module_id"],
                module__course_id=self.kwargs["course_id"],
            )
        )
