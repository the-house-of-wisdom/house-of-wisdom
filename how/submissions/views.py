"""API endpoints for how.submissions"""

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from how.mixins.views import (
    ActionPermissionsMixin,
    ActionSerializersMixin,
    UserFilterMixin,
)
from how.permissions import DenyAll, IsEnrolledOrInstructor, IsOwner
from how.submissions.models import Submission
from how.submissions.serializers import (
    SubmissionCreateSerializer,
    SubmissionSerializer,
)


# Create your views here.
class BaseSubmissionVS(ActionPermissionsMixin, ModelViewSet):
    """Base ViewSet for extension"""

    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    search_fields = ["owner", "assignment"]
    ordering_fields = ["grade", "created_at", "updated_at"]
    filterset_fields = ["owner", "assignment", "grade"]
    action_permissions = {"default": permission_classes}

    def perform_create(self, serializer) -> None:
        """Create and grade a submission

        Args:
            serializer (Serializer): The validated data
        """

        graded = serializer.save(
            owner_id=self.request.user.pk,
            assignment_id=self.kwargs["assignment_id"],
        ).calc_grade()

        if graded:
            graded.save()

    @action(methods=["post"], detail=True)
    def grade(self, request: Request, pk: int) -> Response:
        """Grade a submission"""

        submission = self.get_object()

        if submission.assignment.is_auto_graded:
            submission.calc_grade().save()

            return Response(
                self.get_serializer()(instance=submission), status=status.HTTP_200_OK
            )

        return Response(
            {"details": "This assignment is not auto graded"}, status=status.HTTP_200_OK
        )


class SubmissionViewSet(UserFilterMixin, BaseSubmissionVS):
    """
    API endpoints for managing Submissions.

    ## Overview

    API endpoints provide full RUD (Retrieve, Update, Delete) functionality for assignment submissions.
    This viewset enables students to submit their completed assignments and allows instructors to view, grade, and
    provide feedback on these submissions. Depending on your assignment requirements, submissions can include text responses,
    file uploads, or both.

    ## Endpoints

    - **List Submissions**
      `GET /api/submissions`
      Retrieves a list of all assignment submissions. You can filter or sort the submissions using query parameters.

    - **Retrieve Submission**
      `GET /api/submissions/{id}`
      Retrieves detailed information for the submission identified by `id`.

    - **Update Submission**
      `PUT /api/submissions/{id}`
      Fully updates an existing submission with the provided information.

    - **Partial Update Submission**
      `PATCH /api/submissions/{id}`
      Applies partial updates to a submission (e.g., updating instructor feedback or grade).

    - **Delete Submission**
      `DELETE /api/submissions/{id}`
      Deletes the submission identified by `id`.

    ## Query Parameters

    - **assignment:**
      Filter submissions by assignment (e.g., `?assignment=1`).

    - **search:**
      Filter submissions by student name, assignment details, or feedback content (e.g., `?search=excellent`).

    - **ordering:**
      Sort submissions by a specific field (e.g., `?ordering=-submitted_at` for the newest submissions first).

    ## Permissions

    - **Students:**
      Can create, view, update, or delete their own submission records.

    - **Instructors/Admins:**
      Can view all submissions, grade assignments, and update submissions with feedback.

    ## Example API Requests

    **List Submissions:**

    ```bash
    curl -X GET /api/submissions \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    **Retrieve a Submission:**

    ```bash
    curl -X POST /api/submissions/1 \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```
    """

    action_permissions = {**BaseSubmissionVS.action_permissions, "create": [DenyAll]}


class AssignmentSubmissions(ActionSerializersMixin, BaseSubmissionVS):
    """
    API endpoints for managing Assignment Submissions.

    ## Overview

    API endpoints provide full CRUD (Create, Retrieve, Update, Delete) functionality for assignment submissions.
    This viewset enables students to submit their completed assignments and allows instructors to view, grade, and
    provide feedback on these submissions. Depending on your assignment requirements, submissions can include text responses,
    file uploads, or both.

    ## Endpoints

    - **List Submissions**
      `GET /api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/assignments/{assignmentId}/submissions`
      Retrieves a list of all assignment submissions. You can filter or sort the submissions using query parameters.

    - **Create Submission**
      `POST /api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/assignments/{assignmentId}/submissions`
      Creates a new submission for an assignment. Requires submission details in the request body.

    - **Retrieve Submission**
      `GET /api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/assignments/{assignmentId}/submissions/{id}`
      Retrieves detailed information for the submission identified by `id`.

    - **Update Submission**
      `PUT /api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/assignments/{assignmentId}/submissions/{id}`
      Fully updates an existing submission with the provided information.

    - **Partial Update Submission**
      `PATCH /api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/assignments/{assignmentId}/submissions/{id}`
      Applies partial updates to a submission (e.g., updating instructor feedback or grade).

    - **Delete Submission**
      `DELETE /api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/assignments/{assignmentId}/submissions/{id}`
      Deletes the submission identified by `id`.

    ## Query Parameters

    - **search:**
      Filter submissions by student name, assignment details, or feedback content (e.g., `?search=excellent`).

    - **ordering:**
      Sort submissions by a specific field (e.g., `?ordering=-submitted_at` for the newest submissions first).

    ## Permissions

    - **Students:**
      Can create, view, update, or delete their own submission records.

    - **Instructors/Admins:**
      Can view all submissions, grade assignments, and update submissions with feedback.

    ## Example API Requests

    **List Submissions:**

    ```bash
    curl -X GET /api/courses/1/modules/1/lessons/1/assignments/1/submissions \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    **Create a Submission:**

    ```bash
    curl -X POST /api/courses/1/modules/1/lessons/1/assignments/1/submissions \\
        -H "Content-Type: application/json" \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE" \\
        -d '{
                "answers": [
                { "question": 1, "answers": [1] },
                { "question": 2, "answers": [3, 5] },
                { "question": 3, "answers": [6, 7] },
                { "question": 4, "answers": [10] }
              ]
            }'
    ```
    """

    action_serializers = {
        "default": SubmissionSerializer,
        "create": SubmissionCreateSerializer,
    }
    action_permissions = {
        **BaseSubmissionVS.action_permissions,
        "list": [IsAuthenticated, IsEnrolledOrInstructor],
        "retrieve": [IsAuthenticated, IsEnrolledOrInstructor, IsOwner],
    }

    def get_queryset(self):
        """Filter queryset by assignment"""

        return (
            super()
            .get_queryset()
            .filter(
                owner_id=self.request.user.id,
                assignment_id=self.kwargs["assignment_id"],
            )
        )
