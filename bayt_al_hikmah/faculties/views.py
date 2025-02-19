"""API endpoints for bayt_al_hikmah.faculties"""

from typing import Any, List
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from bayt_al_hikmah.faculties.models import Faculty
from bayt_al_hikmah.faculties.serializers import FacultySerializer


# Create your views here.
class FacultyViewSet(ModelViewSet):
    """Create, view, update and delete Faculties"""

    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "headline", "description"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["name"]

    def get_permissions(self) -> List[Any]:
        if self.action not in ["list", "retrieve"]:
            self.permission_classes = [IsAuthenticated, IsAdminUser]

        return super().get_permissions()
