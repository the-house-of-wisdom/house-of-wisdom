"""API endpoints for bayt_al_hikmah.courses"""

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.courses.models import Course
from bayt_al_hikmah.courses.serializers import CourseSerializer
from bayt_al_hikmah.mixins.views import ActionPermissionsMixin, OwnerMixin
from bayt_al_hikmah.permissions import IsInstructor, IsOwner


# Create your views here.
class CourseViewSet(ActionPermissionsMixin, OwnerMixin, ModelViewSet):
    """Create, view, update and delete Courses"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "headline", "description"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["user", "category", "tags"]
    instructor_permissions = permission_classes + [IsInstructor, IsOwner]
    action_permissions = {
        "default": permission_classes,
        "create": instructor_permissions,
        "update": instructor_permissions,
        "partial_update": instructor_permissions,
        "delete": instructor_permissions,
    }

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
                    f"You joined the course '{course}' successfully"
                    if enrolled
                    else f"You unenrolled from {course}"
                )
            },
            status=status.HTTP_200_OK,
        )
