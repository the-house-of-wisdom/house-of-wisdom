"""API endpoints for bayt_al_hikmah.submissions"""

from typing import Any, List
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.mixins import UserFilterMixin
from bayt_al_hikmah.permissions import IsOwner
from bayt_al_hikmah.submissions.models import Submission
from bayt_al_hikmah.submissions.serializers import SubmissionSerializer


# Create your views here.
class SubmissionViewSet(UserFilterMixin, ModelViewSet):
    """Create, view, update and delete Submissions"""

    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["user", "assignment"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["user", "assignment", "grade"]

    def perform_create(self, serializer) -> None:
        """Create and grade a submission

        Args:
            serializer (Serializer): The validated data
        """

        submission = serializer.save(user=self.request.user)
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

    def get_queryset(self):
        """Filter queryset by user"""

        return (
            super()
            .get_queryset()
            .filter(
                Q(assignment__lesson__module__course__user_id=self.request.user.pk)
                | Q(assignment__lesson__module__course__students=self.request.user)
            )
        )
