""" API endpoints for learn.specializations """

from typing import Any
from django.http import FileResponse, HttpRequest
from django.views.generic import DetailView
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from learn.mixins import OwnerMixin
from learn.permissions import IsOwner
from learn.specializations.models import Specialization
from learn.specializations.serializers import SpecializationSerializer


# Create your views here.
class SpecializationViewSet(OwnerMixin, ModelViewSet):
    """Create, view, update and delete Specializations"""

    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "headline", "description"]
    ordering_fields = ["id", "name", "created_at", "updated_at"]
    filterset_fields = ["name", "is_approved"]

    @action(methods=["post", "get"], detail=True)
    def approve(self, request, pk):
        """Approve a specialization"""

        if not request.user.is_staff:
            return Response(
                {"details": "Only admins can approve specializations"},
                status=status.HTTP_403_FORBIDDEN,
            )

        specialization = self.get_object()
        message: str = f"Specialization {specialization.name} "

        if specialization.is_approved:
            message += "disapproved"
            specialization.is_approved = False
        else:
            message += "approved"
            specialization.is_approved = True

        specialization.save()

        return Response({"details": message})

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes += [IsOwner]
        elif self.action in ["approve"]:
            self.permission_classes += [IsAdminUser]

        return super().get_permissions()


class SpecializationImageView(DetailView):
    """Specialization image"""

    model = Specialization

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> FileResponse:
        return FileResponse(open(self.get_object(self.queryset).image.url[1:], "rb"))
