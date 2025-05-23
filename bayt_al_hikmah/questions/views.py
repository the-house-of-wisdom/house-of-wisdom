"""API endpoints for bayt_al_hikmah.questions"""

import random
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.mixins.views import ActionPermissionsMixin
from bayt_al_hikmah.permissions import (
    DenyAll,
    IsEnrolledOrInstructor,
    IsInstructor,
    IsQuestionOwner,
)
from bayt_al_hikmah.questions.models import Question
from bayt_al_hikmah.questions.serializers import QuestionSerializer
from bayt_al_hikmah.ui.mixins import UserQuestionsMixin


# Create your views here.
class BaseQuestionVS(ActionPermissionsMixin, ModelViewSet):
    """Base ViewSet for extension"""

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsInstructor]
    search_fields = ["text"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["assignment", "type"]
    action_permissions = {
        "default": permission_classes,
        "create": permission_classes + [IsQuestionOwner],
    }


class QuestionViewSet(UserQuestionsMixin, BaseQuestionVS):
    """View, update and delete Questions"""

    action_permissions = {**BaseQuestionVS.action_permissions, "create": [DenyAll]}


class AssignmentQuestions(BaseQuestionVS):
    """Create, view, update and delete Assignment Questions"""

    action_permissions = {
        "default": [IsAuthenticated, IsInstructor, IsQuestionOwner],
        "list": [IsAuthenticated, IsEnrolledOrInstructor],
        "retrieve": [IsAuthenticated, IsEnrolledOrInstructor],
    }

    def perform_create(self, serializer):
        """Add assignment to question automatically"""

        serializer.save(assignment_id=self.kwargs["assignment_id"])

    def get_queryset(self):
        """Filter queryset by assignment"""

        queryset = (
            super()
            .get_queryset()
            .filter(
                assignment_id=self.kwargs["assignment_id"],
                assignment__lesson_id=self.kwargs["lesson_id"],
                assignment__lesson__module_id=self.kwargs["module_id"],
                assignment__lesson__module__course_id=self.kwargs["course_id"],
            )
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
