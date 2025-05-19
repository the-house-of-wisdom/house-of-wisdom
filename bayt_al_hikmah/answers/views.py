"""API endpoints for bayt_al_hikmah.answers"""

from typing import Any, List
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.answers.models import Answer
from bayt_al_hikmah.answers.serializers import AnswerSerializer
from bayt_al_hikmah.permissions import IsInstructor
from bayt_al_hikmah.ui.mixins import UserAnswersMixin


# Create your views here.
class AnswerViewSet(UserAnswersMixin, ModelViewSet):
    """Create, view, update and delete Answers"""

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["text"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["question", "is_correct"]

    def get_permissions(self) -> List[Any]:
        if self.action not in ["list", "retrieve"]:
            self.permission_classes = [IsAuthenticated, IsInstructor]

        return super().get_permissions()
