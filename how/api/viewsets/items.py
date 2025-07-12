"""API endpoints for how.apps.items"""

from ast import Module

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from wagtail.api.v2.views import PagesAPIViewSet

from how.api.mixins import ActionPermissionsMixin, UserFilterMixin
from how.api.permissions import DenyAll, IsEnrolledOrInstructor, IsInstructor, IsOwner
from how.apps.courses.models import Course
from how.apps.items.models import Item
from how.apps.lessons.models import Lesson


# Create your views here.
class BaseItemVS(ActionPermissionsMixin, PagesAPIViewSet):
    """Base ViewSet for extension"""

    model = Item
    name = "items"
    permission_classes = [IsAuthenticated, IsInstructor]
    ordering_fields = ["order", "created_at", "updated_at"]
    filterset_fields = ["type"]
    action_permissions = {
        "default": permission_classes,
        "create": permission_classes + [IsOwner],
    }

    @action(methods=["post"], detail=True)
    def mark(self, request: Request, pk: int) -> Response:
        """Mark a course lesson item as un/completed"""

        is_completed = False
        item = self.get_object()

        if not request.user.items.contains(item):
            is_completed = True
            request.user.items.add(item)

        else:
            request.user.items.remove(item)

        item.save()

        return Response(
            {
                "details": f"Item '{item}' marked as {'completed' if is_completed else 'uncompleted'}"
            },
            status=status.HTTP_200_OK,
        )


class ItemViewSet(UserFilterMixin, BaseItemVS):
    """
    API endpoints for managing Items.

    ## Overview

    API endpoints handle RUD (Retrieve, Update, Delete) operations for lesson items within a lesson.
    Lesson items represent smaller sections of a lesson, such as individual text passages, videos, quizzes, or interactive activities.

    ## Endpoints

    - **List Lesson Items**
      `GET /api/items`
      Retrieves a list of all lesson items.

    - **Retrieve Lesson Item**
      `GET /api/items/{id}`
      Retrieves detailed information for the lesson item identified by `id`.

    - **Update Lesson Item**
      `PUT /api/items/{id}`
      Fully updates an existing lesson item.

    - **Partial Update Lesson Item**
      `PATCH /api/items/{id}`
      Applies partial updates to the lesson item.

    - **Delete Lesson Item**
      `DELETE /api/items/{id}`
      Deletes the lesson item identified by `id`.

    ## Query Parameters

    - **lesson:**
      Filter lesson items by lesson (e.g., `?lesson=1`).

    - **type:**
      Filter lesson items by type (e.g., `?type=1`).

    - **search:**
      Filter lesson items by title or content (e.g., `?search=introduction`).

    - **ordering:**
      Sort items by a specific field (e.g., `?ordering=order` for sequence sorting).

    ## Permissions

    - **Instructors/Admins:**
      Can create, update, and delete lesson items.

    ## Extra Actions

    This viewset includes additional actions to enhance functionality:

    - **Mark Item as Completed:**
      Allows a student to mark an individual lesson item as completed.
      `POST /api/items/{id}/mark`
      *Request:* No body required.
      *Response:* Returns confirmation of completion.

    ## Example API Requests

    **List Lesson Items:**

    ```bash
    curl -X GET /api/items \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    **Create a Lesson Item:**

    ```bash
    curl -X POST /api/items \\
        -H "Content-Type: application/json" \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE" \\
        -d '{
                "lesson": 3,
                "title": "Understanding Variables",
                "content": "This section explains variables in Python.",
                "item_type": "text",
                "order": 1
            }'
    ```

    **Mark Item as Completed:**

    ```bash
    curl -X POST /api/items/1/mark
    ```
    """

    action_permissions = {**BaseItemVS.action_permissions, "create": [DenyAll]}


class LessonItems(BaseItemVS):
    """
    API endpoints for managing Lesson Items.

    ## Overview

    API endpoints handle CRUD (Create, Retrieve, Update, Delete) operations for lesson items within a lesson.
    Lesson items represent smaller sections of a lesson, such as individual text passages, videos, quizzes, or interactive activities.

    ## Endpoints

    - **List Lesson Items**
      `GET /api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/items`
      Retrieves a list of all lesson items.

    - **Create Lesson Item**
      `POST /api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/items`
      Creates a new lesson item within a lesson. Requires details in the request body.

    - **Retrieve Lesson Item**
      `GET /api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/items/{id}`
      Retrieves detailed information for the lesson item identified by `id`.

    - **Update Lesson Item**
      `PUT /api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/items/{id}`
      Fully updates an existing lesson item.

    - **Partial Update Lesson Item**
      `PATCH /api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/items/{id}`
      Applies partial updates to the lesson item.

    - **Delete Lesson Item**
      `DELETE /api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/items/{id}`
      Deletes the lesson item identified by `id`.

    ## Query Parameters

    - **type:**
      Filter lesson items by type (e.g., `?type=1`).

    - **search:**
      Filter lesson items by title or content (e.g., `?search=introduction`).

    - **ordering:**
      Sort items by a specific field (e.g., `?ordering=order` for sequence sorting).

    ## Permissions

    - **Authenticated Users:**
      Can view lesson items within their enrolled courses.

    - **Instructors/Admins:**
      Can create, update, and delete lesson items.

    ## Extra Actions

    This viewset includes additional actions to enhance functionality:

    - **Mark Item as Completed:**
      Allows a student to mark an individual lesson item as completed.
      `POST /api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/items/{id}/mark`
      *Request:* No body required.
      *Response:* Returns confirmation of completion.

    ## Example API Requests

    **List Lesson Items:**

    ```bash
    curl -X GET /api/courses/1/modules/1/lessons/1/items \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    **Create a Lesson Item (Reading):**

    ```bash
    curl -X POST /api/courses/1/modules/1/lessons/1/items \\
        -H "Content-Type: application/json" \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE" \\
        -d '{
                "type": 0,
                "title": "Understanding Variables",
                "content": "This section explains variables in Python."
            }'
    ```

    **Mark Item as Completed:**

    ```bash
    curl -X POST /api/courses/1/modules/1/lessons/1/items/1/mark \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```
    """

    action_permissions = {
        "default": [IsAuthenticated, IsInstructor, IsOwner],
        "list": [IsAuthenticated, IsEnrolledOrInstructor],
        "retrieve": [IsAuthenticated, IsEnrolledOrInstructor],
        "mark": [IsAuthenticated, IsEnrolledOrInstructor],
    }

    def perform_create(self, serializer):
        """Add lesson to item automatically"""

        Lesson.objects.get(pk=self.kwargs["lesson_id"]).add_child(
            instance=Item(**serializer.validated_data, owner_id=self.request.user.pk)
        )

    def get_queryset(self):
        """Filter queryset by lesson"""

        return (
            super()
            .get_queryset()
            .descendant_of(Course.objects.get(pk=self.kwargs["course_id"]))
            .descendant_of(Module.objects.get(pk=self.kwargs["module_id"]))
            .child_of(Lesson.objects.get(pk=self.kwargs["lesson_id"]))
        )
