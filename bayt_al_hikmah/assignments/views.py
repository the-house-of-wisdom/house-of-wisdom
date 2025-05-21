"""API endpoints for bayt_al_hikmah.assignments"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.assignments.models import Assignment
from bayt_al_hikmah.assignments.serializers import AssignmentSerializer
from bayt_al_hikmah.mixins.views import ActionPermDictMixin
from bayt_al_hikmah.permissions import DenyAll, IsAssignmentOwner, IsInstructor
from bayt_al_hikmah.ui.mixins import UserAIMixin


# Create your views here.
class BaseAssignmentVS(ActionPermDictMixin, UserAIMixin, ModelViewSet):
    """Base ViewSet for extension"""

    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated, IsInstructor]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["lesson__module__course", "lesson__module", "lesson"]
    action_perm_dict = {
        "default": permission_classes,
        "create": permission_classes + [IsAssignmentOwner],
    }


class AssignmentViewSet(BaseAssignmentVS):
    """View, update and delete Assignments"""

    action_perm_dict = {**BaseAssignmentVS.action_perm_dict, "create": [DenyAll]}


class LessonAssignmentsVS(BaseAssignmentVS):
    """Create, view, update and delete Lesson Assignments"""

    def perform_create(self, serializer):
        """Add lesson to assignment automatically"""

        serializer.save(lesson_id=self.kwargs["lesson_id"])

    def get_queryset(self):
        """Filter queryset by lesson"""

        return super().get_queryset().filter(lesson_id=self.kwargs["lesson_id"])
