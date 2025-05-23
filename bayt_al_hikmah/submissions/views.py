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
    """Create, view, update and delete Submissions"""

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
    """View, update and delete Submissions"""

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
    """Create, view, update and delete Assignment Submissions"""

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
