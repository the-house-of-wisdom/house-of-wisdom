"""API endpoints for how.assignments"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from how.assignments.models import Assignment
from how.assignments.serializers import AssignmentSerializer
from how.courses.models import Course
from how.lessons.models import Lesson
from how.mixins.views import ActionPermissionsMixin, UserFilterMixin
from how.modules.models import Module
from how.permissions import (
    DenyAll,
    IsOwner,
    IsEnrolledOrInstructor,
    IsInstructor,
)


# Create your views here.
class BaseAssignmentVS(ActionPermissionsMixin, ModelViewSet):
    """Base ViewSet for extension"""

    queryset = Assignment.objects.live()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated, IsInstructor]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at", "updated_at", "order"]
    filterset_fields = ["type"]
    action_permissions = {
        "default": permission_classes,
        "create": permission_classes + [IsOwner],
    }


class AssignmentViewSet(UserFilterMixin, BaseAssignmentVS):
    """
    API endpoints for managing Lesson Assignments.

    ## Overview

    API endpoints provide RUD (Retrieve, Update, Delete) functionality for assignments within a lesson.
    Assignments serve as assessments for learners and can include written tasks, quizzes, coding exercises, or practical applications.

    ## Endpoints

    - **List Assignments**
      `GET /api/assignments`
      Retrieves a list of all assignments.

    - **Retrieve Assignment**
      `GET /api/assignments/{id}`
      Retrieves detailed information for an assignment identified by `id`.

    - **Update Assignment**
      `PUT /api/assignments/{id}`
      Fully updates an existing assignment.

    - **Partial Update Assignment**
      `PATCH /api/assignments/{id}`
      Applies partial updates to assignment attributes.

    - **Delete Assignment**
      `DELETE /api/assignments/{id}`
      Deletes the assignment identified by `id`.

    ## Query Parameters

    - **lesson:**
      Filter assignments by lesson (e.g., `?lesson=1`).

    - **type:**
      Filter assignments by type (e.g., `?type=1`).

    - **search:**
      Filter assignments by title or content (e.g., `?search=project`).

    - **ordering:**
      Sort assignments by a specific field (e.g., `?ordering=-due_date` for upcoming deadlines first).

    - **Instructors/Admins:**
      Can create, update, and delete assignments.

    ## Example API Requests

    **List Assignments:**

    ```bash
    curl -X GET /api/assignments \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    **Retrieve an Assignment:**

    ```bash
    curl -X POST /api/assignments/1
    ```

    > **🔹 Info:** Be sure to check the [`AssignmentInstanceAPI`](/api/courses/1/modules/1/lessons/1/assignments/1/).
    """

    action_permissions = {**BaseAssignmentVS.action_permissions, "create": [DenyAll]}


class LessonAssignments(BaseAssignmentVS):
    """
    API endpoints for managing Lesson Assignments.

    ## Overview

    API endpoints provide CRUD (Create, Retrieve, Update, Delete) functionality for assignments within a lesson.
    Assignments serve as assessments for learners and can include written tasks, quizzes, coding exercises, or practical applications.

    ## Endpoints

    - **List Assignments**
      `GET /api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/assignments`
      Retrieves a list of all assignments.

    - **Create Assignment**
      `POST /api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/assignments`
      Creates a new assignment within a lesson. Requires assignment details in the request body.

    - **Retrieve Assignment**
      `GET /api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/assignments/{id}`
      Retrieves detailed information for an assignment identified by `id`.

    - **Update Assignment**
      `PUT /api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/assignments/{id}`
      Fully updates an existing assignment.

    - **Partial Update Assignment**
      `PATCH /api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/assignments/{id}`
      Applies partial updates to assignment attributes.

    - **Delete Assignment**
      `DELETE /api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/assignments/{id}`
      Deletes the assignment identified by `id`.

    ## Query Parameters

    - **type:**
      Filter assignments by type (e.g., `?type=1`).

    - **search:**
      Filter assignments by title or content (e.g., `?search=project`).

    - **ordering:**
      Sort assignments by a specific field (e.g., `?ordering=-due_date` for upcoming deadlines first).

    ## Permissions

    - **Students:**
      Can view and submit assignments within lessons they are enrolled in.

    - **Instructors/Admins:**
      Can create, update, and delete assignments.

    ## Example API Requests

    **List Assignments:**

    ```bash
    curl -X GET /api/courses/1/modules/1/lessons/1/assignments \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    **Create an Assignment with type of Quiz:**

    ```bash
    curl -X POST /api/courses/1/modules/1/lessons/1/assignments \\
        -H "Content-Type: application/json" \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE" \\
        -d '{
                "type": 0,
                "title": "Final Project Submission",
                "description": "The final assignment in the course",
                "content": "Submit your project following the provided guidelines.",
            }'
    ```
    """

    action_permissions = {
        "default": [IsAuthenticated, IsInstructor, IsOwner],
        "list": [IsAuthenticated, IsEnrolledOrInstructor],
        "retrieve": [IsAuthenticated, IsEnrolledOrInstructor],
    }

    def perform_create(self, serializer):
        """Add lesson to assignment automatically"""

        Lesson.objects.get(pk=self.kwargs["lesson_id"]).add_child(
            instance=Assignment(
                **serializer.validated_data, owner_id=self.request.user.pk
            )
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
