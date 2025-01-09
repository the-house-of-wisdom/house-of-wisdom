""" API endpoints for bayt_al_hikmah.assignments """

from typing import Any, List
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.assignments.models import Assignment
from bayt_al_hikmah.assignments.serializers import AssignmentSerializer


# Create your views here.
class AssignmentViewSet(ModelViewSet):
    """Create, view, update and delete Assignments"""

    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["lesson__module__course", "lesson__module", "lesson", "type"]

    def get_permissions(self) -> List[Any]:
        if self.action not in ["list", "retrieve"]:
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()
