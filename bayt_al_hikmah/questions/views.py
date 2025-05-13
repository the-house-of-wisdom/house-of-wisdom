"""API endpoints for bayt_al_hikmah.questions"""

from typing import Any, List
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.permissions import IsInstructor
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
            self.permission_classes = [IsAuthenticated, IsInstructor]

        return super().get_permissions()

    def get_queryset(self):
        """Filter queryset by user"""

        return (
            super()
            .get_queryset()
            .filter(
                Q(assignment__lesson__module__course__user_id=self.request.user.pk)
                | Q(assignment__lesson__module__course__students=self.request.user)
            )
        )
