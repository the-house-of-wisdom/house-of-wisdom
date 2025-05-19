"""API endpoints for bayt_al_hikmah.paths"""

from typing import Any, List
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.mixins import OwnerMixin, UserFilterMixin
from bayt_al_hikmah.paths.models import Path
from bayt_al_hikmah.paths.serializers import PathSerializer
from bayt_al_hikmah.permissions import IsInstructor, IsOwner


# Create your views here.
class PathViewSet(OwnerMixin, UserFilterMixin, ModelViewSet):
    """Create, view, update and delete Paths"""

    queryset = Path.objects.all()
    serializer_class = PathSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "headline", "description"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["user", "category", "tags"]

    def get_permissions(self) -> List[Any]:
        if self.action not in ["list", "retrieve", "enroll"]:
            self.permission_classes = [IsAuthenticated, IsInstructor, IsOwner]

        return super().get_permissions()

    @action(methods=["post"], detail=True)
    def save(self, request: Request, pk: int) -> Response:
        """Add a path to favorite or saved paths"""

        saved: bool = False
        path: Path = self.get_object()

        if request.user.saved.contains(path):
            request.user.saved.remove(path)

        else:
            saved = True
            request.user.saved.add(path)

        return Response(
            {
                "details": f"Path '{path}' {'added to' if saved else 'removed from'} your saved paths"
            },
            status=status.HTTP_200_OK,
        )
