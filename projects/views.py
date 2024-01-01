""" API endpoints for learn.projects """


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
from learn.projects.models import Project
from learn.projects.serializers import ProjectSerializer


# Create your views here.
class ProjectViewSet(OwnerMixin, ModelViewSet):
    """Create, view, update and delete Projects"""

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "headline", "description"]
    ordering_fields = ["id", "name", "created_at", "updated_at"]
    filterset_fields = ["name"]

    @action(methods=["post", "get"], detail=True)
    def approve(self, request, pk):
        """Approve a Project"""

        if not request.user.is_staff:
            return Response(
                {"details": "Only admins can approve Projects"},
                status=status.HTTP_403_FORBIDDEN,
            )

        Project = self.get_object()
        message: str = f"Project {Project.name} "

        if Project.is_approved:
            message += "disapproved"
            Project.is_approved = False
        else:
            message += "approved"
            Project.is_approved = True

        Project.save()

        return Response({"details": message})

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes += [IsOwner]
        elif self.action in ["approve", "list"]:
            self.permission_classes += [IsAdminUser]

        return super().get_permissions()


class ProjectImageView(DetailView):
    """Project profile image"""

    model = Project

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> FileResponse:
        return FileResponse(open(self.get_object(self.queryset).image.url[1:], "rb"))
