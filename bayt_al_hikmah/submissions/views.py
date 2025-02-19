"""API endpoints for bayt_al_hikmah.submissions"""

from typing import Any, List
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from bayt_al_hikmah.submissions.models import Submission
from bayt_al_hikmah.submissions.serializers import SubmissionSerializer


# Create your views here.
class SubmissionViewSet(ModelViewSet):
    """Create, view, update and delete Submissions"""

    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["user", "assignment"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["user", "assignment", "grade"]

    def get_permissions(self) -> List[Any]:
        if self.action not in ["list", "retrieve"]:
            self.permission_classes = [IsAuthenticated, IsAdminUser]

        return super().get_permissions()
