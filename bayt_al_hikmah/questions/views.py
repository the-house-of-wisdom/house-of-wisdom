""" API endpoints for bayt_al_hikmah.questions """

from typing import Any, List
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from bayt_al_hikmah.questions.models import Question
from bayt_al_hikmah.questions.serializers import QuestionSerializer


# Create your views here.
class QuestionViewSet(ModelViewSet):
    """Create, view, update and delete Questions"""

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["text"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["assignment", "type"]

    def get_permissions(self) -> List[Any]:
        if self.action not in ["list", "retrieve"]:
            self.permission_classes = [IsAuthenticated, IsAdminUser]

        return super().get_permissions()
