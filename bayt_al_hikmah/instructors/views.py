""" API endpoints for bayt_al_hikmah.instructors """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.mixins import OwnerMixin
from bayt_al_hikmah.instructors.models import Instructor
from bayt_al_hikmah.instructors.serializers import InstructorSerializer
from bayt_al_hikmah.permissions import IsOwner


# Create your views here.
class InstructorViewSet(OwnerMixin, ModelViewSet):
    """Create, view, update and delete learning paths"""

    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["user", "institute"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["user", "institute"]

    def get_permissions(self):
        if self.action not in ["list", "retrieve"]:
            self.permission_classes = [IsAuthenticated, IsOwner]

        return super().get_permissions()
