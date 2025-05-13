"""API endpoints for bayt_al_hikmah.answers"""

from typing import Any, List
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.answers.models import Answer
from bayt_al_hikmah.answers.serializers import AnswerSerializer
from bayt_al_hikmah.permissions import IsInstructor


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
            self.permission_classes = [IsAuthenticated, IsInstructor]

        return super().get_permissions()

    def get_queryset(self):
        """Filter queryset by user"""

        return (
            super()
            .get_queryset()
            .filter(
                Q(
                    question__assignment__lesson__module__course__user_id=self.request.user.pk
                )
                | Q(
                    question__assignment__lesson__module__course__students=self.request.user
                )
            )
        )
