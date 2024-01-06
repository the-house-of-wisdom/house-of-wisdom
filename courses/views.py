""" API endpoints for learn.courses """


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
from learn.courses.models import Course
from learn.courses.serializers import CourseSerializer
from learn.specializations.models import Specialization


# Create your views here.
class CourseViewSet(OwnerMixin, ModelViewSet):
    """Create, view, update and delete Courses"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "headline", "description"]
    ordering_fields = ["id", "name", "created_at", "updated_at"]
    filterset_fields = ["specialization", "name", "is_approved"]

    @action(methods=["post", "get"], detail=True)
    def approve(self, request, pk):
        """Approve a Course"""

        if not request.user.is_staff:
            return Response(
                {"details": "Only admins can approve Courses"},
                status=status.HTTP_403_FORBIDDEN,
            )

        course = self.get_object()
        message: str = f"Course {course.name} "

        if course.is_approved:
            message += "disapproved"
            course.is_approved = False
        else:
            message += "approved"
            course.is_approved = True

        course.save()

        return Response({"details": message})

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes += [IsOwner]
        elif self.action in ["approve"]:
            self.permission_classes += [IsAdminUser]

        return super().get_permissions()


class CourseImageView(DetailView):
    """Course profile image"""

    model = Course

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> FileResponse:
        return FileResponse(open(self.get_object(self.queryset).image.url[1:], "rb"))


class SpecializationCoursesViewSet(CourseViewSet):
    """Courses of a specialization"""

    def get_queryset(self):
        """Filter queryset by specialization"""

        specialization = Specialization.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(specialization=specialization)

    def perform_create(self, serializer):
        """Adds a course to a specialization"""
        specialization = Specialization.objects.get(pk=self.kwargs["id"])
        serializer.save(specialization=specialization)
