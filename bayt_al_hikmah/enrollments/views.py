"""API endpoints for bayt_al_hikmah.enrollments"""

from typing import Any, List
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from bayt_al_hikmah.enrollments.models import Enrollment
from bayt_al_hikmah.enrollments.serializers import EnrollmentSerializer


# Create your views here.
class EnrollmentViewSet(ModelViewSet):
    """Create, view, update and delete Enrollments"""

    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["course", "user"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["user", "specialization", "course", "is_approved", "role"]

    def get_permissions(self) -> List[Any]:
        if self.action not in ["list", "retrieve"]:
            self.permission_classes = [IsAuthenticated, IsAdminUser]

        return super().get_permissions()
