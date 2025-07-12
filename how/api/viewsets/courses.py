"""API endpoints for how.apps.courses"""

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from wagtail.api.v2.views import PagesAPIViewSet

from how.api.mixins import ActionPermissionsMixin, OwnerMixin
from how.api.permissions import IsInstructor, IsOwner
from how.apps.courses.models import Course


# Create your views here.
class CourseViewSet(ActionPermissionsMixin, OwnerMixin, PagesAPIViewSet):
    """
    API endpoints for managing Course records.

    ## Overview

    API endpoints provide full CRUD (Create, Retrieve, Update, Delete) functionality for the Course model.
    It enables authenticated users to view course information and allows administrative users to create, update, or delete courses.

    ## Endpoints

    - **List Courses**
    `GET /api/courses`
    Retrieves a list of all courses.

    - **Create Course**
    `POST /api/courses`
    Creates a new course. Requires course details in the request body.

    - **Retrieve Course**
    `GET /api/courses/{id}`
    Retrieves detailed information for the course identified by `id`.

    - **Update Course**
    `PUT /api/courses/{id}`
    Fully updates an existing course with the provided information.

    - **Partial Update**
    `PATCH /api/courses/{id}`
    Applies partial updates to an existing course.

    - **Delete Course**
    `DELETE /api/courses/{id}`
    Deletes the course identified by `id`.

    ## Query Parameters

    - **search:**
    Filter courses by title or description (e.g., `?search=python`).

    - **ordering:**
    Order the results by a specific field (e.g., `?ordering=-created_at` for reverse chronological order).

    ## Permissions

    - **Authenticated Users:**
    Can view the list of courses and retrieve individual course details.

    - **Admin/Staff Users:**
    Can create, update, and delete courses.

    ## Extra Actions

    In addition to the default CRUD operations, this viewset defines several custom actions to extend its functionality:

    - **Un/Enroll from/in a Course:**
    Allows an authenticated user to un/enroll from/in a course.
    `POST /api/courses/{id}/enroll`
    *Request:* No body is required.
    *Response:* Returns a confirmation message.

    ## Example API Requests

    **List Courses:**

    ```bash
    curl -X GET /api/courses \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    **Create a Course:**

    ```bash
    curl -X POST /api/courses \\
        -H "Content-Type: application/json" \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE" \\
        -d '{
                "category": 1,
                "image": "path/to/image.png",
                "title": "Introduction to Python",
                "headline": "Master Python Basics",
                "description": "Learn the basics of Python programming.",
                "tags": [1, 3, 5]  // Array of tag IDs associated with the course
            }'
    ```

    > **🔹 Info:** Be sure to check the [`CourseInstanceAPI`](/api/courses/1/).
    """

    model = Course
    name = "courses"
    permission_classes = [IsAuthenticated]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["owner"]
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
