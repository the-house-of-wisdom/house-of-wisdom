"""API endpoints for bayt_al_hikmah.modules"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.mixins.views import ActionPermissionsMixin
from bayt_al_hikmah.modules.models import Module
from bayt_al_hikmah.modules.serializers import ModuleSerializer
from bayt_al_hikmah.permissions import (
    DenyAll,
    IsEnrolledOrInstructor,
    IsInstructor,
    IsModuleOwner,
)
from bayt_al_hikmah.ui.mixins import UserModulesMixin


# Create your views here.
class BaseModuleVS(ActionPermissionsMixin, ModelViewSet):
    """Base ViewSet for extension"""

    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated, IsInstructor]
    search_fields = ["title", "description"]
    ordering_fields = ["title", "order", "created_at", "updated_at"]
    filterset_fields = ["course"]
    action_permissions = {"default": permission_classes}


class ModuleViewSet(UserModulesMixin, BaseModuleVS):
    """
    API endpoints for managing Modules.

    ## Overview

    API endpoints provide RUD (Retrieve, Update, Delete) functionality for modules within a course.
    Modules represent structured segments of a course and typically contain lessons, resources, and assessments.

    ## Endpoints

    - **List Modules**
    `GET /api/modules`
    Retrieves a list of all course modules.

    - **Retrieve Module**
    `GET /api/modules/{id}`
    Retrieves detailed information for the module identified by `id`.

    - **Update Module**
    `PUT /api/modules/{id}`
    Fully updates an existing module with new details.

    - **Partial Update Module**
    `PATCH /api/modules/{id}`
    Applies partial updates to module attributes.

    - **Delete Module**
    `DELETE /api/modules/{id}`
    Deletes the module identified by `id`.

    ## Query Parameters

    - **course:**
    Filter modules by course (e.g., `?course=1`).

    - **search:**
    Filter modules by title or description (e.g., `?search=basics`).

    - **ordering:**
    Order the results by a specific field (e.g., `?ordering=order` to sort by module sequence).

    ## Permissions

    - **Instructors/Admins:**
    Can create, update, and delete modules within their courses.

    ## Example API Requests

    **List Modules:**

    ```bash
    curl -X GET http://localhost:8000/api/modules \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    **Retrieve a Module:**

    ```bash
    curl -X GET http://localhost:8000/api/modules/1 \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    > **🔹 Info:** Be sure to check the [`ModuleInstanceAPI`](/api/courses/1/modules/1/).
    """

    action_permissions = {**BaseModuleVS.action_permissions, "create": [DenyAll]}


class CourseModules(BaseModuleVS):
    """
    API endpoints for managing Course Modules.

    ## Overview

    API endpoints provide CRUD (Create, Retrieve, Update, Delete) functionality for modules within a course.
    Modules represent structured segments of a course and typically contain lessons, resources, and assessments.

    ## Endpoints

    - **List Modules**
    `GET /api/courses/{courseId}/modules`
    Retrieves a list of all course modules.

    - **Create Module**
    `POST /api/courses/{courseId}/modules`
    Creates a new module within a course. Requires module details in the request body.

    - **Retrieve Module**
    `GET /api/courses/{courseId}/modules/{id}`
    Retrieves detailed information for the module identified by `id`.

    - **Update Module**
    `PUT /api/courses/{courseId}/modules/{id}`
    Fully updates an existing module with new details.

    - **Partial Update Module**
    `PATCH /api/courses/{courseId}/modules/{id}`
    Applies partial updates to module attributes.

    - **Delete Module**
    `DELETE /api/courses/{courseId}/modules/{id}`
    Deletes the module identified by `id`.

    ## Query Parameters

    - **search:**
    Filter modules by title or description (e.g., `?search=basics`).

    - **ordering:**
    Order the results by a specific field (e.g., `?ordering=order` to sort by module sequence).

    ## Permissions

    - **Authenticated Users:**
    Can view module details.

    - **Instructors/Admins:**
    Can create, update, and delete modules within their courses.

    ## Example API Requests

    **List Modules:**

    ```bash
    curl -X GET http://localhost:8000/api/courses/1/modules \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    **Create a Module:**

    ```bash
    curl -X POST http://localhost:8000/api/courses/1/modules \\
        -H "Content-Type: application/json" \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE" \\
        -d '{
                "title": "Introduction to Web Development",
                "description": "Foundational topics in HTML, CSS, and JavaScript",
                "order": 1
            }'
    ```
    """

    action_permissions = {
        "default": [IsAuthenticated, IsInstructor, IsModuleOwner],
        "list": [IsAuthenticated, IsEnrolledOrInstructor],
        "retrieve": [IsAuthenticated, IsEnrolledOrInstructor],
    }

    def perform_create(self, serializer):
        """Create a module with course set automatically"""

        serializer.save(course_id=self.kwargs["course_id"])

    def get_queryset(self):
        """Filter queryset by course"""

        return super().get_queryset().filter(course_id=self.kwargs["course_id"])
