"""API endpoints for how.apps.lessons"""

from rest_framework.permissions import IsAuthenticated
from wagtail.api.v2.views import PagesAPIViewSet

from how.api.mixins import ActionPermissionsMixin, UserFilterMixin
from how.api.permissions import DenyAll, IsEnrolledOrInstructor, IsInstructor, IsOwner
from how.apps.courses.models import Course
from how.apps.lessons.models import Lesson
from how.apps.modules.models import Module


# Create your views here.
class BaseLessonVS(ActionPermissionsMixin, PagesAPIViewSet):
    """Base ViewSet for extension"""

    model = Lesson
    name = "lessons"
    permission_classes = [IsAuthenticated, IsInstructor]
    ordering_fields = ["title", "order", "created_at", "updated_at"]
    action_permissions = {
        "default": permission_classes,
        "create": permission_classes + [IsOwner],
    }


class LessonViewSet(UserFilterMixin, BaseLessonVS):
    """
    API endpoints for managing Lessons within Modules.

    ## Overview

    API endpoints provide RUD (Retrieve, Update, Delete) functionality for lessons within a module.
    Lessons form the core instructional content of a module and may include text-based materials, videos, quizzes, or interactive exercises.

    ## Endpoints

    - **List Lessons**
      `GET /api/lessons`
      Retrieves a list of all lessons.

    - **Retrieve Lesson**
      `GET /api/lessons/{id}`
      Retrieves detailed information for the lesson identified by `id`.

    - **Update Lesson**
      `PUT /api/lessons/{id}`
      Fully updates an existing lesson with new details.

    - **Partial Update Lesson**
      `PATCH /api/lessons/{id}`
      Applies partial updates to lesson attributes.

    - **Delete Lesson**
      `DELETE /api/lessons/{id}`
      Deletes the lesson identified by `id`.

    ## Query Parameters

    - **module:**
      Filter lessons by title or content keywords (e.g., `?module=1`).

    - **search:**
      Filter lessons by title or description (e.g., `?search=arrays`).

    - **ordering:**
      Order lessons by a specific field (e.g., `?ordering=order` to list lessons in sequence).

    ## Permissions

    - **Instructors/Admins:**
      Can create, update, and delete lessons.

    ## Example API Requests

    **List Lessons:**

    ```bash
    curl -X GET /api/lessons \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    > **🔹 Info:** Be sure to check the [`LessonInstanceAPI`](/api/courses/1/modules/1/lessons/1/).
    """

    action_permissions = {**BaseLessonVS.action_permissions, "create": [DenyAll]}


class ModuleLessons(BaseLessonVS):
    """
    API endpoints for managing Lessons within Course Modules.

    ## Overview

    API endpoints provide CRUD (Create, Retrieve, Update, Delete) functionality for lessons within a module.
    Lessons form the core instructional content of a module and may include text-based materials, videos, quizzes, or interactive exercises.

    ## Endpoints

    - **List Lessons**
      `GET /api/courses/{courseId}/modules/{moduleId}/lessons`
      Retrieves a list of all lessons.

    - **Create Lesson**
      `POST /api/courses/{courseId}/modules/{moduleId}/lessons`
      Creates a new lesson within a module. Requires lesson details in the request body.

    - **Retrieve Lesson**
      `GET /api/courses/{courseId}/modules/{moduleId}/lessons/{id}`
      Retrieves detailed information for the lesson identified by `id`.

    - **Update Lesson**
      `PUT /api/courses/{courseId}/modules/{moduleId}/lessons/{id}`
      Fully updates an existing lesson with new details.

    - **Partial Update Lesson**
      `PATCH /api/courses/{courseId}/modules/{moduleId}/lessons/{id}`
      Applies partial updates to lesson attributes.

    - **Delete Lesson**
      `DELETE /api/courses/{courseId}/modules/{moduleId}/lessons/{id}`
      Deletes the lesson identified by `id`.

    ## Query Parameters

    - **search:**
      Filter lessons by title or description (e.g., `?search=arrays`).

    - **ordering:**
      Order lessons by a specific field (e.g., `?ordering=order` to list lessons in sequence).

    ## Permissions

    - **Authenticated Users:**
      Can view lessons within their enrolled courses.

    - **Instructors/Admins:**
      Can create, update, and delete lessons.

    ## Example API Requests

    **List Lessons:**

    ```bash
    curl -X GET /api/courses/1/lessons \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    **Create a Lesson:**

    ```bash
    curl -X POST /api/courses/1/lessons \\
        -H "Content-Type: application/json" \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE" \\
        -d '{
                "module": 2,
                "title": "Introduction to Data Structures",
                "description": "Understanding arrays, linked lists, and trees.",
                "order": 1
            }'
    ```
    """

    action_permissions = {
        "default": [IsAuthenticated, IsInstructor, IsOwner],
        "list": [IsAuthenticated, IsEnrolledOrInstructor],
        "retrieve": [IsAuthenticated, IsEnrolledOrInstructor],
    }

    def perform_create(self, serializer):
        """Create a lesson with module set automatically"""

        Module.objects.get(pk=self.kwargs["module_id"]).add_child(
            instance=Lesson(**serializer.validated_data, owner_id=self.request.user.pk)
        )

    def get_queryset(self):
        """Filter queryset by module"""

        return (
            super()
            .get_queryset()
            .descendant_of(Course.objects.get(pk=self.kwargs["course_id"]))
            .child_of(Module.objects.get(pk=self.kwargs["module_id"]))
        )
