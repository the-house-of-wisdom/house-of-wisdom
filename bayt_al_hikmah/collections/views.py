"""API endpoints for bayt_al_hikmah.collections"""

from typing import Any, List
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.mixins import OwnerMixin
from bayt_al_hikmah.collections.models import Collection
from bayt_al_hikmah.collections.serializers import CollectionSerializer
from bayt_al_hikmah.permissions import IsInstructor, IsOwner


# Create your views here.
class CollectionViewSet(OwnerMixin, ModelViewSet):
    """Create, view, update and delete Collections"""

    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "headline", "description"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["user", "category", "tags"]

    def get_permissions(self) -> List[Any]:
        if self.action not in ["list", "retrieve", "enroll"]:
            self.permission_classes = [IsAuthenticated, IsInstructor, IsOwner]

        return super().get_permissions()

    def get_queryset(self):
        """Filter queryset by user"""

        return (
            super()
            .get_queryset()
            .filter(Q(user_id=self.request.user.pk) | Q(savers=self.request.user))
        )

    @action(methods=["post"], detail=True)
    def save(self, request: Request, pk: int) -> Response:
        """Add a collection to favorite or saved collections"""

        saved: bool = False
        collection: Collection = self.get_object()

        if request.user.saved.contains(collection):
            request.user.saved.remove(collection)

        else:
            saved = True
            request.user.saved.add(collection)

        return Response(
            {
                "details": f"Collection '{collection}' {'added to' if saved else 'removed from'} your saved collections"
            },
            status=status.HTTP_200_OK,
        )
