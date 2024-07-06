""" API endpoints for learn.accomplishments """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from learn.mixins import OwnerMixin
from learn.permissions import IsOwner
from learn.accomplishments.models import Accomplishment
from learn.accomplishments.serializers import AccomplishmentSerializer


# Create your views here.
class AccomplishmentViewSet(OwnerMixin, ModelViewSet):
    """Create, view, update and delete Accomplishments"""

    queryset = Accomplishment.objects.all()
    serializer_class = AccomplishmentSerializer
    permission_classes = [IsAuthenticated]
    search_fields = []
    ordering_fields = ["id", "created_at", "updated_at"]
    filterset_fields = ["user", "specialization", "course", "item"]

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes += [IsOwner]

        return super().get_permissions()
