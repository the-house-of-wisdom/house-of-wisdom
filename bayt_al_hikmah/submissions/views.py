"""API endpoints for bayt_al_hikmah.submissions"""

from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.mixins.views import ActionPermissionsMixin, ActionSerializersMixin
from bayt_al_hikmah.permissions import DenyAll, IsEnrolledOrInstructor, IsOwner
from bayt_al_hikmah.submissions.models import Submission
from bayt_al_hikmah.submissions.serializers import (
    SubmissionCreateSerializer,
    SubmissionSerializer,
)


# Create your views here.
class BaseSubmissionVS(ActionPermissionsMixin, ModelViewSet):
    """Base ViewSet for extension"""

    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    search_fields = ["user", "assignment"]
    ordering_fields = ["grade", "created_at", "updated_at"]
    filterset_fields = ["user", "assignment", "grade"]
    action_permissions = {"default": permission_classes}

    def perform_create(self, serializer) -> None:
        """Create and grade a submission

        Args:
            serializer (Serializer): The validated data
        """

        submission = serializer.save(
            user=self.request.user, assignment_id=self.kwargs["assignment_id"]
        )
        questions = [
            {
                "question": q.id,
                # Check if ids of answers and ids of submission answers are equal
                "is_correct": [
                    i[0] for i in q.answers.filter(is_correct=True).values_list("id")
                ]
                == list(filter(lambda a: a["question"] == q.id, submission.answers))[0][
                    "answers"
                ],
                # Generate question feedback
                "feedback": [
                    {
                        "id": a.id,
                        "text": a.text,
                        "content": a.description,
                    }
                    for a in q.answers.filter(
                        id__in=list(
                            filter(lambda a: a["question"] == q.id, submission.answers)
                        )[0]["answers"]
                    )
                ],
            }
            for q in submission.assignment.questions.all()
        ]

        submission.feedback = questions
        submission.grade = (
            len(list(filter(lambda q: q["is_correct"], questions)))
            / submission.assignment.questions.count()
            * 100
        )
        submission.save()


class SubmissionViewSet(BaseSubmissionVS):
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
    curl -X GET http://localhost:8000/api/submissions \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    **Retrieve a Submission:**

    ```bash
    curl -X POST http://localhost:8000/api/submissions/1 \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```
    """

    action_permissions = {**BaseSubmissionVS.action_permissions, "create": [DenyAll]}

    def get_queryset(self):
        """
        Filter queryset by user to allow users to view their submissions only and
        allow instructors to view submissions of their assignments.
        """

        return (
            super()
            .get_queryset()
            .filter(
                Q(user_id=self.request.user.id)
                | Q(assignment__lesson__module__course__user_id=self.request.user.id)
            )
        )


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
    curl -X GET http://localhost:8000/api/courses/1/modules/1/lessons/1/assignments/1/submissions \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    **Create a Submission:**

    ```bash
    curl -X POST http://localhost:8000/api/courses/1/modules/1/lessons/1/assignments/1/submissions \\
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
                user_id=self.request.user.id,
                assignment_id=self.kwargs["assignment_id"],
                assignment__lesson_id=self.kwargs["lesson_id"],
                assignment__lesson__module_id=self.kwargs["module_id"],
                assignment__lesson__module__course_id=self.kwargs["course_id"],
            )
        )
