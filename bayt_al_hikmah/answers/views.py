"""API endpoints for bayt_al_hikmah.answers"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.answers.models import Answer
from bayt_al_hikmah.answers.serializers import AnswerSerializer
from bayt_al_hikmah.mixins.views import ActionPermissionsMixin
from bayt_al_hikmah.permissions import DenyAll, IsAnswerOwner, IsInstructor
from bayt_al_hikmah.ui.mixins import UserAnswersMixin


# Create your views here.
class BaseAnswerVS(ActionPermissionsMixin, ModelViewSet):
    """Base ViewSet for extension"""

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, IsInstructor]
    search_fields = ["text"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["question", "is_correct"]
    action_permissions = {
        "default": permission_classes,
        "create": permission_classes + [IsAnswerOwner],
    }


class AnswerViewSet(UserAnswersMixin, BaseAnswerVS):
    """
    API endpoints for managing Answers.

    ## Overview

    API endpoints provide full RUD (Retrieve, Update, Delete) functionality for answer to assignment questions.
    This viewset enables students to submit their responses and allows instructors to review, grade, and provide feedback on those answers.

    ## Endpoints

    - **List Answers**
      `GET /api/answers`
      Retrieves a list of all answer for assignment questions.

    - **Retrieve Answer**
      `GET /api/answers/{id}`
      Retrieves detailed information for a specific answer identified by `id`.

    - **Update Answer**
      `PUT /api/answers/{id}`
      Fully updates an existing answer.

    - **Partial Update Answer**
      `PATCH /api/answers/{id}`
      Applies partial updates to an answer (e.g., adding instructor feedback).

    - **Delete Answer**
      `DELETE /api/answers/{id}`
      Deletes the answer identified by `id`.

    ## Query Parameters

    - **question:**
      Filter answers by `question` (e.g., `?question=1`).

    - **search:**
      Filter answers by keywords in `text` (e.g., `?search=variable`).

    - **ordering:**
      Sort answers by a specific field (e.g., `?ordering=-created_at` for newest first).

    ## Permissions

    - **Instructors/Admins:**
      Can list, review, update and delete all answer.

    ## Example API Requests

    **List Answers:**

    ```bash
    curl -X GET http://localhost:8000/api/answers \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```
    """

    action_permissions = {**BaseAnswerVS.action_permissions, "create": [DenyAll]}


class QuestionAnswers(BaseAnswerVS):
    """
    API endpoints for managing Assignment Question Answers.

    ## Overview

    API endpoints provide full CRUD (Create, Retrieve, Update, Delete) functionality for answer to assignment questions.
    This viewset enables instructors to review, and provide feedback on those answers.

    ## Endpoints

    - **List Answers**
      `GET /api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/assignments/{assignmentId}/questions/{questionId}/answers`
      Retrieves a list of all answer for assignment questions.

    - **Create Answer (Submit Answer)**
      `POST /api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/assignments/{assignmentId}/questions/{questionId}/answers`
      Creates a new answer. Typically used when an instructor adds an answer for a question.

    - **Retrieve Answer**
      `GET /api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/assignments/{assignmentId}/questions/{questionId}/answers/{id}`
      Retrieves detailed information for a specific answer identified by `id`.

    - **Update Answer**
      `PUT /api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/assignments/{assignmentId}/questions/{questionId}/answers/{id}`
      Fully updates an existing answer.

    - **Partial Update Answer**
      `PATCH /api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/assignments/{assignmentId}/questions/{questionId}/answers/{id}`
      Applies partial updates to an answer (e.g., adding instructor feedback).

    - **Delete Answer**
      `DELETE /api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/assignments/{assignmentId}/questions/{questionId}/answers/{id}`
      Deletes the answer identified by `id`.

    ## Query Parameters

    - **question:**
      Filter answers by `question` (e.g., `?question=1`).

    - **search:**
      Filter answers by keywords in `text` (e.g., `?search=variable`).

    - **ordering:**
      Sort answers by a specific field (e.g., `?ordering=-created_at` for newest first).

    ## Permissions

    - **Instructors/Admins:**
      Can list, review, grade, and update all answer.

    ## Example API Requests

    **List Answers:**

    ```bash
    curl -X GET http://localhost:8000/api/courses/1/modules/1/lessons/1/assignments/1/questions/1/answers \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```
    """

    action_permissions = {"default": [IsAuthenticated, IsInstructor, IsAnswerOwner]}

    def perform_create(self, serializer):
        """Add question to answer automatically"""

        serializer.save(question_id=self.kwargs["question_id"])

    def get_queryset(self):
        """Filter queryset by question"""

        return (
            super()
            .get_queryset()
            .filter(
                question_id=self.kwargs["question_id"],
                question__assignment_id=self.kwargs["assignment_id"],
                question__assignment__lesson_id=self.kwargs["lesson_id"],
                question__assignment__lesson__module_id=self.kwargs["module_id"],
                question__assignment__lesson__module__course_id=self.kwargs[
                    "course_id"
                ],
            )
        )
