"""API endpoints for bayt_al_hikmah.questions"""

import random
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.assignments.models import Assignment
from bayt_al_hikmah.courses.models import Course
from bayt_al_hikmah.lessons.models import Lesson
from bayt_al_hikmah.mixins.views import ActionPermissionsMixin, UserFilterMixin
from bayt_al_hikmah.modules.models import Module
from bayt_al_hikmah.permissions import DenyAll, IsInstructor, IsOwner
from bayt_al_hikmah.questions.models import Question
from bayt_al_hikmah.questions.serializers import QuestionSerializer


# Create your views here.
class BaseQuestionVS(ActionPermissionsMixin, ModelViewSet):
    """Base ViewSet for extension"""

    queryset = Question.objects.live()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsInstructor]
    search_fields = ["text"]
    ordering_fields = ["order", "created_at", "updated_at"]
    filterset_fields = ["type"]
    action_permissions = {
        "default": permission_classes,
        "create": permission_classes + [IsOwner],
    }


class QuestionViewSet(UserFilterMixin, BaseQuestionVS):
    """
    API endpoints for managing Questions.

    ## Overview

    API endpoints provide RUD (Retrieve, Update, Delete) functionality for questions within an assignment.
    These questions can be structured as multiple-choice, short answer, coding exercises, or other formats depending on the assignment type.

    ## Endpoints

    - **List Assignment Questions**
      `GET /api/questions`
      Retrieves a list of all questions across assignments.

    - **Create Assignment Question**
      `POST /api/questions`
      Creates a new question within an assignment. Requires details in the request body.

    - **Retrieve Assignment Question**
      `GET /api/questions/{id}`
      Retrieves detailed information for a specific question identified by `id`.

    - **Update Assignment Question**
      `PUT /api/questions/{id}`
      Fully updates an existing question.

    - **Partial Update Assignment Question**
      `PATCH /api/questions/{id}`
      Applies partial updates to a question's attributes.

    - **Delete Assignment Question**
      `DELETE /api/questions/{id}`
      Deletes the question identified by `id`.

    ## Query Parameters

    - **assignment:**
      Filter questions by assignment (e.g., `?assignment=1`).

    - **search:**
      Filter questions by text content (e.g., `?search=python`).

    - **ordering:**
      Sort questions by a specific field (e.g., `?ordering=order` for sequential arrangement).

    ## Permissions

    - **Instructors/Admins:**
      Can create, update, and delete assignment questions.

    ## Example API Requests

    **List Assignment Questions:**

    ```bash
    curl -X GET /api/questions \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    **Retrieve an Assignment Question:**

    ```bash
    curl -X POST /api/questions/1 \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    > **🔹 Info:** Be sure to check the [`QuestionInstanceAPI`](/api/courses/1/modules/1/lessons/1/assignments/1/).
    """

    action_permissions = {**BaseQuestionVS.action_permissions, "create": [DenyAll]}


class AssignmentQuestions(BaseQuestionVS):
    """
    API endpoints for managing Assignment Questions.

    ## Overview

    API endpoints provide CRUD (Create, Retrieve, Update, Delete) functionality for questions within an assignment.
    These questions can be structured as multiple-choice, short answer, coding exercises, or other formats depending on the assignment type.

    ## Endpoints

    - **List Assignment Questions**
      `GET /api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/assignments/{assignmentId}/questions`
      Retrieves a list of all questions across assignments.

    - **Create Assignment Question**
      `POST /api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/assignments/{assignmentId}/questions`
      Creates a new question within an assignment. Requires details in the request body.

    - **Retrieve Assignment Question**
      `GET /api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/assignments/{assignmentId}/questions/{id}`
      Retrieves detailed information for a specific question identified by `id`.

    - **Update Assignment Question**
      `PUT /api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/assignments/{assignmentId}/questions/{id}`
      Fully updates an existing question.

    - **Partial Update Assignment Question**
      `PATCH /api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/assignments/{assignmentId}/questions/{id}`
      Applies partial updates to a question's attributes.

    - **Delete Assignment Question**
      `DELETE /api/courses/{courseId}/modules/{moduleId}/lessons/{lessonId}/assignments/{assignmentId}/questions/{id}`
      Deletes the question identified by `id`.

    ## Query Parameters

    - **type:**
      Filter questions by type (e.g., `?type=1`).

    - **search:**
      Filter questions by text content (e.g., `?search=python`).

    - **ordering:**
      Sort questions by a specific field (e.g., `?ordering=order` for sequential arrangement).

    ## Permissions

    - **Students:**
      Can view questions within assignments they are enrolled in.

    - **Instructors/Admins:**
      Can create, update, and delete assignment questions.

    ## Example API Requests

    **List Assignment Questions:**

    ```bash
    curl -X GET /api/courses/1/modules/1/lessons/1/assignments/1/questions \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    **Create an Assignment Question:**

    ```bash
    curl -X POST /api/courses/1/modules/1/lessons/1/assignments/1/questions \\
        -H "Content-Type: application/json" \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE" \\
        -d '{
                "text": "What is the output of print(2 + 2)?",
                "type": 0
            }'
    ```
    """

    action_permissions = {"default": [IsAuthenticated, IsInstructor, IsOwner]}

    def perform_create(self, serializer):
        """Add assignment to question automatically"""

        Assignment.objects.get(pk=self.kwargs["assignment_id"]).add_child(
            instance=Question(
                **serializer.validated_data, owner_id=self.request.user.pk
            )
        )

    def get_queryset(self):
        """Filter queryset by assignment"""

        queryset = (
            super()
            .get_queryset()
            .descendant_of(Course.objects.get(pk=self.kwargs["course_id"]))
            .descendant_of(Module.objects.get(pk=self.kwargs["module_id"]))
            .descendant_of(Lesson.objects.get(pk=self.kwargs["lesson_id"]))
            .child_of(Assignment.objects.get(pk=self.kwargs["assignment_id"]))
        )

        if self.request.GET.get("randomize"):
            question = queryset.first()
            assignment = question.assignment if question else None

            if assignment:
                # Max number of questions to display
                max_q_count = assignment.question_count

                if max_q_count < queryset.count():
                    # Get ids of questions
                    q_ids = [q[0] for q in queryset.values_list("id")]

                    # Select random questions
                    choices = random.choices(q_ids, k=max_q_count)

                    # TODO: Check if required number of questions are selected
                    choice_count = len(choices)
                    if choice_count <= max_q_count:
                        choices.extend(
                            random.choices(
                                list(filter(lambda q: q not in choices, q_ids)),
                                k=(max_q_count - choice_count) * 5,
                            )
                        )

                    return queryset.filter(id__in=choices)

        return queryset
