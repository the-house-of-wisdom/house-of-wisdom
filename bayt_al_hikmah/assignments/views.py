"""API endpoints for bayt_al_hikmah.assignments"""

from typing import Any, List
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.assignments.models import Assignment
from bayt_al_hikmah.assignments.serializers import AssignmentSerializer
from bayt_al_hikmah.permissions import IsInstructor


# Create your views here.
class AssignmentViewSet(ModelViewSet):
    """Create, view, update and delete Assignments"""

    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["lesson__module__course", "lesson__module", "lesson"]

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
                Q(lesson__module__course__user_id=self.request.user.pk)
                | Q(lesson__module__course__students=self.request.user)
            )
        )
