"""API endpoints for bayt_al_hikmah.assignments"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.assignments.models import Assignment
from bayt_al_hikmah.assignments.serializers import AssignmentSerializer
from bayt_al_hikmah.mixins.views import ActionPermissionsMixin
from bayt_al_hikmah.permissions import (
    DenyAll,
    IsAssignmentOwner,
    IsEnrolledOrInstructor,
    IsInstructor,
)
from bayt_al_hikmah.ui.mixins import UserAssignmentsMixin


# Create your views here.
class BaseAssignmentVS(ActionPermissionsMixin, ModelViewSet):
    """Base ViewSet for extension"""

    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated, IsInstructor]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["lesson__module__course", "lesson__module", "lesson"]
    action_permissions = {
        "default": permission_classes,
        "create": permission_classes + [IsAssignmentOwner],
    }


class AssignmentViewSet(UserAssignmentsMixin, BaseAssignmentVS):
    """View, update and delete Assignments"""

    action_permissions = {**BaseAssignmentVS.action_permissions, "create": [DenyAll]}


class LessonAssignments(BaseAssignmentVS):
    """Create, view, update and delete Lesson Assignments"""

    action_permissions = {
        "default": [IsAuthenticated, IsInstructor, IsAssignmentOwner],
        "list": [IsAuthenticated, IsEnrolledOrInstructor],
        "retrieve": [IsAuthenticated, IsEnrolledOrInstructor],
    }

    def perform_create(self, serializer):
        """Add lesson to assignment automatically"""

        serializer.save(lesson_id=self.kwargs["lesson_id"])

    def get_queryset(self):
        """Filter queryset by lesson"""

        return (
            super()
            .get_queryset()
            .filter(
                lesson_id=self.kwargs["lesson_id"],
                lesson__module_id=self.kwargs["module_id"],
                lesson__module__course_id=self.kwargs["course_id"],
            )
        )
