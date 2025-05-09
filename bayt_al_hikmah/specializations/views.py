"""API endpoints for bayt_al_hikmah.specializations"""

from typing import Any, List
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from bayt_al_hikmah.specializations.models import Specialization
from bayt_al_hikmah.specializations.serializers import SpecializationSerializer
from bayt_al_hikmah.permissions import IsOwner


# Create your views here.
class SpecializationViewSet(ModelViewSet):
    """Create, view, update and delete Specializations"""

    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "headline", "description"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["user", "category", "tags"]

    def get_permissions(self) -> List[Any]:
        if self.action not in ["list", "retrieve"]:
            self.permission_classes = [IsAuthenticated, IsAdminUser, IsOwner]

        return super().get_permissions()

    @action(methods=["post"], detail=True)
    def enroll(self, request: Request, pk: int) -> Response:
        """Enroll in a specialization"""

        enrolled: bool = False
        specialization: Specialization = self.get_object()

        if specialization.students.contains(request.user):
            specialization.students.remove(request.user)

        else:
            enrolled = True
            specialization.students.add(request.user)

            # First course in specialization
            course = specialization.courses.first()

            if not course.students.contains(request.user):
                course.students.add(request.user)

        return Response(
            {
                "details": (
                    "Your enrollment request sent"
                    if enrolled
                    else f"You unenrolled from {specialization}"
                )
            },
            status=status.HTTP_200_OK,
        )
