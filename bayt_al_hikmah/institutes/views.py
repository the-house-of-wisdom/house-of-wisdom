""" API endpoints for bayt_al_hikmah.institutes """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.mixins import OwnerMixin
from bayt_al_hikmah.institutes.models import Institute
from bayt_al_hikmah.institutes.serializers import InstituteSerializer
from bayt_al_hikmah.permissions import IsOwner


# Create your views here.
class InstituteViewSet(OwnerMixin, ModelViewSet):
    """Create, view, update and delete Institutes"""

    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "headline", "description"]
    ordering_fields = ["name", "created_at", "updated_at"]
    filterset_fields = ["name"]

    def get_permissions(self):
        if self.action not in ["list", "retrieve"]:
            self.permission_classes = [IsAuthenticated, IsOwner]

        return super().get_permissions()
