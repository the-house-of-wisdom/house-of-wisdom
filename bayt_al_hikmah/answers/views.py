"""API endpoints for bayt_al_hikmah.answers"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.answers.models import Answer
from bayt_al_hikmah.answers.serializers import AnswerSerializer
from bayt_al_hikmah.mixins.views import ActionPermissionsMixin
from bayt_al_hikmah.permissions import (
    DenyAll,
    IsAnswerOwner,
    IsEnrolledOrInstructor,
    IsInstructor,
)
from bayt_al_hikmah.ui.mixins import UserAnswersMixin


# Create your views here.
class BaseAnswerVS(ActionPermissionsMixin, ModelViewSet):
    """Base ViewSet for extension"""

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, IsInstructor]
    search_fields = ["text"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["question", "is_correct"]
    action_permissions = {
        "default": permission_classes,
        "create": permission_classes + [IsAnswerOwner],
    }


class AnswerViewSet(UserAnswersMixin, BaseAnswerVS):
    """View, update and delete Answers"""

    action_permissions = {**BaseAnswerVS.action_permissions, "create": [DenyAll]}


class QuestionAnswers(BaseAnswerVS):
    """Create, view, update and delete Question Answers"""

    action_permissions = {
        "default": [IsAuthenticated, IsInstructor, IsAnswerOwner],
        "list": [IsAuthenticated, IsEnrolledOrInstructor],
        "retrieve": [IsAuthenticated, IsEnrolledOrInstructor],
    }

    def perform_create(self, serializer):
        """Add question to answer automatically"""

        serializer.save(question_id=self.kwargs["question_id"])

    def get_queryset(self):
        """Filter queryset by question"""

        return (
            super()
            .get_queryset()
            .filter(
                question_id=self.kwargs["question_id"],
                question__assignment_id=self.kwargs["assignment_id"],
                question__assignment__lesson_id=self.kwargs["lesson_id"],
                question__assignment__lesson__module_id=self.kwargs["module_id"],
                question__assignment__lesson__module__course_id=self.kwargs[
                    "course_id"
                ],
            )
        )
