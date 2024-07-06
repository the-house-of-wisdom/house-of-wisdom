""" API endpoints for learn.instructors """

from typing import Any
from django.http import FileResponse, HttpRequest
from django.views.generic import DetailView
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from learn.mixins import OwnerMixin
from learn.permissions import IsOwner
from learn.instructors.models import Instructor
from learn.instructors.serializers import InstructorSerializer


# Create your views here.
class InstructorViewSet(OwnerMixin, ModelViewSet):
    """Create, view, update and delete Instructors"""

    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "description"]
    ordering_fields = ["id", "name", "created_at", "updated_at"]
    filterset_fields = ["user", "name", "is_approved"]

    @action(methods=["post", "get"], detail=True)
    def approve(self, request, pk):
        """Approve an Instructor"""

        if not request.user.is_staff:
            return Response(
                {"details": "Only admins can approve instructors"},
                status=status.HTTP_403_FORBIDDEN,
            )

        instructor = self.get_object()
        message: str = f"Instructor {instructor.name} "

        if instructor.is_approved:
            message += "disapproved"
            instructor.is_approved = False
        else:
            message += "approved"
            instructor.is_approved = True

        instructor.save()

        return Response({"details": message})

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes += [IsOwner]
        elif self.action == "approve":
            self.permission_classes += [IsAdminUser]

        return super().get_permissions()


class InstructorImageView(DetailView):
    """Instructor profile image"""

    model = Instructor

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> FileResponse:
        return FileResponse(open(self.get_object(self.queryset).image.url[1:], "rb"))
