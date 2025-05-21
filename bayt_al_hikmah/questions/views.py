"""API endpoints for bayt_al_hikmah.questions"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.mixins.views import ActionPermDictMixin
from bayt_al_hikmah.permissions import DenyAll, IsInstructor, IsQuestionOwner
from bayt_al_hikmah.questions.models import Question
from bayt_al_hikmah.questions.serializers import QuestionSerializer
from bayt_al_hikmah.ui.mixins import UserQuestionsMixin


# Create your views here.
class BaseQuestionVS(ActionPermDictMixin, UserQuestionsMixin, ModelViewSet):
    """Base ViewSet for extension"""

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsInstructor]
    search_fields = ["text"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["assignment", "type"]
    action_perm_dict = {
        "default": permission_classes,
        "create": permission_classes + [IsQuestionOwner],
    }


class QuestionViewSet(BaseQuestionVS):
    """View, update and delete Questions"""

    action_perm_dict = {**BaseQuestionVS.action_perm_dict, "create": [DenyAll]}


class AssignmentQuestionsVS(BaseQuestionVS):
    """Create, view, update and delete Assignment Questions"""

    def perform_create(self, serializer):
        """Add assignment to question automatically"""

        serializer.save(assignment_id=self.kwargs["assignment_id"])

    def get_queryset(self):
        """Filter queryset by assignment"""

        return super().get_queryset().filter(assignment_id=self.kwargs["assignment_id"])
