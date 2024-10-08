""" API endpoints for bayt_al_hikmah.paths """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.mixins import OwnerMixin
from bayt_al_hikmah.paths.models import Path
from bayt_al_hikmah.paths.serializers import PathSerializer


# Create your views here.
class PathViewSet(OwnerMixin, ModelViewSet):
    """Create, view, update and delete learning paths"""

    queryset = Path.objects.all()
    serializer_class = PathSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "headline", "description"]
    ordering_fields = ["id", "name", "created_at", "updated_at"]
    filterset_fields = ["name", "is_approved"]
