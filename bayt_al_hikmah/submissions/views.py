"""API endpoints for bayt_al_hikmah.submissions"""

from typing import Any, List
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.mixins.views import ActionPermDictMixin, UserFilterMixin
from bayt_al_hikmah.permissions import DenyAll, IsOwner
from bayt_al_hikmah.submissions.models import Submission
from bayt_al_hikmah.submissions.serializers import SubmissionSerializer


# Create your views here.
class BaseSubmissionVS(ActionPermDictMixin, ModelViewSet):
    """Create, view, update and delete Submissions"""

    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    search_fields = ["user", "assignment"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["user", "assignment", "grade"]
    action_perm_dict = {"default": permission_classes}

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
                    i["id"] for i in q.answers.filter(is_correct=True).values("id")
                ]
                == list(filter(lambda a: a["question"] == q.id, submission.answers))[0][
                    "answers"
                ],
                # Generate question feedback
                "feedback": [
                    {
                        "answer": a.id,
                        "is_correct": a.is_correct,
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

    def get_permissions(self) -> List[Any]:
        if self.action not in ["list", "retrieve"]:
            self.permission_classes = [IsAuthenticated, IsOwner]

        return super().get_permissions()


class SubmissionViewSet(UserFilterMixin, BaseSubmissionVS):
    """View, update and delete Submissions"""

    action_perm_dict = {**BaseSubmissionVS.action_perm_dict, "create": [DenyAll]}


class AssignmentSubmissionsVS(BaseSubmissionVS):
    """Create, view, update and delete Assignment Submissions"""

    def get_queryset(self):
        """Filter queryset by assignment"""

        return super().get_queryset().filter(assignment_id=self.kwargs["assignment_id"])
