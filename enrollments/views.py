""" API endpoints for learn.enrollments """

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from learn.mixins import OwnerMixin
from learn.permissions import IsOwner
from learn.courses.models import Course
from learn.enrollments.models import Enrollment
from learn.enrollments.serializers import EnrollmentSerializer
from learn.specializations.models import Specialization


# Create your views here.
class EnrollmentViewSet(OwnerMixin, ModelViewSet):
    """Create, view, update and delete Enrollments"""

    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    search_fields = []
    ordering_fields = ["id", "created_at", "updated_at"]
    filterset_fields = ["user", "specialization", "course"]

    def get_permissions(self):
        if self.action in ["approve"]:
            self.permission_classes += [IsAdminUser]

        return super().get_permissions()

    @action(methods=["post", "get"], detail=True)
    def approve(self, request, pk):
        """Approve an enrolment"""

        if not request.user.is_staff:
            return Response(
                {"details": "Only admins can approve enrollments"},
                status=status.HTTP_403_FORBIDDEN,
            )

        enrollment = self.get_object()
        message: str = f"Enrollment {enrollment} "

        if enrollment.is_approved:
            message += "disapproved"
            enrollment.is_approved = False
        else:
            message += "approved"
            enrollment.is_approved = True

        enrollment.save()

        return Response({"details": message})


class SpecializationEnrollmentsViewSet(EnrollmentViewSet):
    """Enrollments of a specialization"""

    def get_queryset(self):
        """Filter queryset by specialization"""

        specialization = Specialization.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(specialization=specialization)

    def perform_create(self, serializer):
        """Add an enrollment to a specialization"""

        specialization = Specialization.objects.get(pk=self.kwargs["id"])
        serializer.save(user=self.request.user, specialization=specialization)
        # serializer.save(user=self.request.user, specialization=specialization.courses.first)


class CourseEnrollmentsViewSet(EnrollmentViewSet):
    """Enrollments of a course"""

    def get_queryset(self):
        """Filter queryset by course"""

        course = Course.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(course=course)

    def perform_create(self, serializer):
        """Add an enrollment to a course"""

        course = Course.objects.get(pk=self.kwargs["id"])
        serializer.save(user=self.request.user, course=course)
