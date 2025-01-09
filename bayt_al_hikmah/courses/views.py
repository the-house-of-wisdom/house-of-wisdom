""" API endpoints for bayt_al_hikmah.courses """

from typing import Any, List
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from bayt_al_hikmah.courses.models import Course
from bayt_al_hikmah.courses.serializers import CourseSerializer
from bayt_al_hikmah.permissions import IsOwner


# Create your views here.
class CourseViewSet(ModelViewSet):
    """Create, view, update and delete Courses"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "headline", "description"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = [
        "user",
        "category",
        "department__faculty",
        "department",
        "specialization",
        "tags",
    ]

    def get_permissions(self) -> List[Any]:
        if self.action not in ["list", "retrieve"]:
            self.permission_classes = [IsAuthenticated, IsAdminUser, IsOwner]

        return super().get_permissions()

    @action(methods=["post"], detail=True)
    def enroll(self, request: Request, pk: int) -> Response:
        """Enroll in a course"""

        enrolled: bool = False
        course: Course = self.get_object()

        if course.students.contains(request.user):
            course.students.remove(request.user)

        else:
            enrolled = True
            course.students.add(request.user)

        return Response(
            {
                "details": (
                    "Your enrollment request sent"
                    if enrolled
                    else f"You unenrolled from {course}"
                )
            },
            status=status.HTTP_200_OK,
        )
