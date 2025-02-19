"""API endpoints for bayt_al_hikmah.answers"""

from typing import Any, List
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from bayt_al_hikmah.answers.models import Answer
from bayt_al_hikmah.answers.serializers import AnswerSerializer


# Create your views here.
class AnswerViewSet(ModelViewSet):
    """Create, view, update and delete Answers"""

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["text"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["question", "is_correct"]

    def get_permissions(self) -> List[Any]:
        if self.action not in ["list", "retrieve"]:
            self.permission_classes = [IsAuthenticated, IsAdminUser]

        return super().get_permissions()
