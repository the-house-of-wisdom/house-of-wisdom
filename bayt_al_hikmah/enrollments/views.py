"""API endpoints for bayt_al_hikmah.enrollments"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.enrollments.models import Enrollment
from bayt_al_hikmah.enrollments.serializers import EnrollmentSerializer
from bayt_al_hikmah.mixins.views import ActionPermissionsMixin, UserFilterMixin
from bayt_al_hikmah.permissions import DenyAll, IsInstructor, IsOwner


# Create your views here.
class BaseEnrollmentVS(ActionPermissionsMixin, ModelViewSet):
    """Base ViewSet for extension"""

    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    search_fields = ["course", "owner"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["owner", "course", "role", "progress", "is_completed"]
    action_permissions = {"default": permission_classes}


class EnrollmentViewSet(UserFilterMixin, BaseEnrollmentVS):
    """
    API endpoints for managing Enrollments.

    ## Overview

    API endpoints provide full RUD (Retrieve, Update, Delete) functionality for course enrollment records.
    This viewset allows students to enroll in courses and enables instructors or administrators to monitor, update,
    and manage enrollments. Each enrollment record links a student with a course and stores relevant metadata, such
    as enrollment date, progress status, and completion information.

    ## Endpoints

    - **List Enrollments**
      `GET /api/enrollments`
      Retrieves a list of all course enrollments. Supports filtering by student, course, and status via query parameters.

    - **Retrieve Enrollment**
      `GET /api/enrollments/{id}`
      Retrieves detailed information for a specific enrollment record identified by `id`.

    - **Update Enrollment**
      `PUT /api/enrollments/{id}`
      Fully updates an existing enrollment record with new details (e.g., progress updates, status changes).

    - **Partial Update Enrollment**
      `PATCH /api/enrollments/{id}`
      Applies partial updates to an enrollment record.

    - **Delete Enrollment (Un-enroll from a Course)**
      `DELETE /api/enrollments/{id}`
      Deletes the enrollment record identified by `id`, effectively un-enrolling the student from the course.

    ## Query Parameters

    - **user:**
      Filter enrollments by student (e.g., `?user=1`).

    - **course:**
      Filter enrollments by course (e.g., `?course=1`).

    - **progress:**
      Filter enrollments by progress (e.g., `?progress=80.0`).

    - **is_completed:**
      Filter enrollments by completion status (e.g., `?is_completed=1`).

    - **role:**
      Filter enrollments by role (e.g., `?role=1`).

    - **search:**
      Filter enrollments by student name, course title (e.g., `?search=python`).

    - **ordering:**
      Order enrollments by a specific field, such as `created_at` or `progress` (e.g., `?ordering=-created_at` for newest enrollments first).

    ## Permissions

    - **Students:**
      Can create (enroll in a course), view, update, or delete only their own enrollment records.

    ## Example API Requests

    **List Course Enrollments:**

    ```bash
    curl -X GET /api/enrollments \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```
    """

    action_permissions = {**BaseEnrollmentVS.action_permissions, "create": [DenyAll]}


class CourseEnrollments(BaseEnrollmentVS):
    """
    API endpoints for managing Course Enrollments.

    ## Overview

    API endpoints provide full CRUD (Create, Retrieve, Update, Delete) functionality for course enrollment records.
    This viewset allows students to enroll in courses and enables instructors or administrators to monitor, update,
    and manage enrollments. Each enrollment record links a student with a course and stores relevant metadata, such
    as enrollment date, progress status, and completion information.

    ## Endpoints

    - **List Enrollments**
      `GET /api/courses/{courseId}/enrollments`
      Retrieves a list of all course enrollments. Supports filtering by student, course, and status via query parameters.

    - **Create Enrollment (Enroll in a Course)**
      `POST /api/courses/{courseId}/enrollments`
      Creates a new enrollment record. Requires details such as the course and student identifiers in the request body.

    - **Retrieve Enrollment**
      `GET /api/courses/{courseId}/enrollments/{id}`
      Retrieves detailed information for a specific enrollment record identified by `id`.

    - **Update Enrollment**
      `PUT /api/courses/{courseId}/enrollments/{id}`
      Fully updates an existing enrollment record with new details (e.g., progress updates, status changes).

    - **Partial Update Enrollment**
      `PATCH /api/courses/{courseId}/enrollments/{id}`
      Applies partial updates to an enrollment record.

    - **Delete Enrollment (Un-enroll from a Course)**
      `DELETE /api/courses/{courseId}/enrollments/{id}`
      Deletes the enrollment record identified by `id`, effectively un-enrolling the student from the course.

    ## Query Parameters

    - **user:**
      Filter enrollments by student (e.g., `?user=1`).

    - **progress:**
      Filter enrollments by progress (e.g., `?progress=80.0`).

    - **is_completed:**
      Filter enrollments by completion status (e.g., `?is_completed=1`).

    - **role:**
      Filter enrollments by role (e.g., `?role=1`).

    - **search:**
      Filter enrollments by student name, course title (e.g., `?search=python`).

    - **ordering:**
      Order enrollments by a specific field, such as `created_at` or `progress` (e.g., `?ordering=-created_at` for newest enrollments first).

    ## Permissions

    - **Instructors/Admins:**
      Can view and manage all enrollment records including updating status or reviewing progress.

    ## Example API Requests

    **List Course Enrollments:**

    ```bash
    curl -X GET /api/courses/1/enrollments \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```
    """

    action_permissions = {"default": [IsAuthenticated, IsInstructor]}

    def perform_create(self, serializer):
        """Add course to enrollment automatically"""

        serializer.save(
            owner_id=self.request.user.pk, course_id=self.kwargs["course_id"]
        )

    def get_queryset(self):
        """Filter queryset by course"""

        return super().get_queryset().filter(course_id=self.kwargs["course_id"])
