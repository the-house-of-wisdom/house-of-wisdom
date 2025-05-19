"""API endpoints for bayt_al_hikmah.enrollments"""

from typing import Any, List
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.enrollments.models import Enrollment
from bayt_al_hikmah.enrollments.serializers import EnrollmentSerializer
from bayt_al_hikmah.mixins import OwnerMixin
from bayt_al_hikmah.permissions import IsOwner


# Create your views here.
class EnrollmentViewSet(OwnerMixin, ModelViewSet):
    """Create, view, update and delete Enrollments"""

    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["course", "user"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["user", "path", "course", "role"]

    def get_permissions(self) -> List[Any]:
        if self.action not in ["list", "retrieve"]:
            self.permission_classes = [IsAuthenticated, IsOwner]

        return super().get_permissions()

    def get_queryset(self):
        """Filter queryset by user"""

        return (
            super()
            .get_queryset()
            .filter(
                Q(user_id=self.request.user.pk)
                | Q(course__user_id=self.request.user.pk)
            )
        )
