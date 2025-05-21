"""API endpoints for bayt_al_hikmah.lessons"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.lessons.models import Lesson
from bayt_al_hikmah.lessons.serializers import LessonSerializer
from bayt_al_hikmah.mixins.views import ActionPermDictMixin
from bayt_al_hikmah.permissions import DenyAll, IsInstructor, IsLessonOwner
from bayt_al_hikmah.ui.mixins import UserLessonsMixin


# Create your views here.
class BaseLessonVS(ActionPermDictMixin, UserLessonsMixin, ModelViewSet):
    """Base ViewSet for extension"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsInstructor]
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["module__course", "module"]
    action_perm_dict = {
        "default": permission_classes,
        "create": permission_classes + [IsLessonOwner],
    }


class LessonViewSet(BaseLessonVS):
    """Create, view, update and delete Lessons"""

    action_perm_dict = {**BaseLessonVS.action_perm_dict, "create": [DenyAll]}


class ModuleLessonsVS(BaseLessonVS):
    """Create, view, update and delete Module Lessons"""

    def perform_create(self, serializer):
        """Create a lesson with module set automatically"""

        serializer.save(module_id=self.kwargs["module_id"])

    def get_queryset(self):
        """Filter queryset by module"""

        return super().get_queryset().filter(module_id=self.kwargs["module_id"])
