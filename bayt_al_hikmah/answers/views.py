"""API endpoints for bayt_al_hikmah.answers"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.answers.models import Answer
from bayt_al_hikmah.answers.serializers import AnswerSerializer
from bayt_al_hikmah.mixins.views import ActionPermDictMixin
from bayt_al_hikmah.permissions import DenyAll, IsAnswerOwner, IsInstructor
from bayt_al_hikmah.ui.mixins import UserAnswersMixin


# Create your views here.
class BaseAnswerVS(ActionPermDictMixin, UserAnswersMixin, ModelViewSet):
    """Base ViewSet for extension"""

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, IsInstructor]
    search_fields = ["text"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["question", "is_correct"]
    action_perm_dict = {
        "default": permission_classes,
        "create": permission_classes + [IsAnswerOwner],
    }


class AnswerViewSet(BaseAnswerVS):
    """View, update and delete Answers"""

    action_perm_dict = {**BaseAnswerVS.action_perm_dict, "create": [DenyAll]}


class QuestionAnswersVS(BaseAnswerVS):
    """Create, view, update and delete Question Answers"""

    def perform_create(self, serializer):
        """Add question to answer automatically"""

        serializer.save(question_id=self.kwargs["question_id"])

    def get_queryset(self):
        """Filter queryset by question"""

        return super().get_queryset().filter(question_id=self.kwargs["question_id"])
