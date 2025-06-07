"""Data Models for how.submissions"""

from typing import Any, Dict, List, Optional, Self
from django.core import validators
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from how.mixins.models import DateTimeMixin


# Create your models here.
User = get_user_model()


def filter_answers(
    answers: List[Dict[str, Any]], question_id: int
) -> List[Dict[str, Any]]:
    """
    Filter answers by question id

    Args:
        answers (List[Dict[str, Any]]): Answers list to be filtered
        question_id (int): Question id

    Returns:
        List[Dict[str, Any]]: Filtered questions
    """

    return list(filter(lambda answer: answer["question"] == question_id, answers))


class Submission(DateTimeMixin, models.Model):
    """Assignment Submissions"""

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="submissions",
        help_text=_("User"),
    )
    assignment = models.ForeignKey(
        "assignments.Assignment",
        on_delete=models.CASCADE,
        related_name="submissions",
        help_text=_("Submission assignment"),
    )
    grade = models.FloatField(
        null=True,
        blank=True,
        help_text=_("Submission grade"),
        validators=[
            validators.MinValueValidator(0.0, "Grade must be >= 0."),
            validators.MaxValueValidator(100.0, "Grade must be <= 100."),
        ],
    )
    answers = models.JSONField(
        help_text=_("Submission answers"),
    )
    feedback = models.JSONField(
        null=True,
        blank=True,
        help_text=_("Submission feedback"),
    )
    file = models.FileField(
        null=True,
        blank=True,
        upload_to="files/submissions/",
        help_text=_("Submission file"),
    )

    @property
    def status(self) -> str:
        """Submission status"""

        return (
            "Pending"
            if self.grade is None
            else "Passed" if self.grade >= self.assignment.min_percentage else "Failed"
        )

    def __str__(self) -> str:
        return f"{self.assignment}: Submission {self.pk} by {self.owner}"

    def calc_grade(self) -> Optional[Self]:
        """Auto grade the submission"""

        a = self.assignment

        # Check if the submission is auto graded
        if not a.is_auto_graded:
            return

        feedback = [
            {
                # Identify questions by id
                "question": q.id,
                # Check if the answer for this questions is correct
                "is_correct": [
                    # Extract the ids of correct answers
                    ans["id"]
                    for ans in q.answers.filter(is_correct=True).values()
                ]
                # Check if the correct answers are selected
                == filter_answers(self.answers, q.id)[0]["answers"],
                # Generate answer feedback
                "answers": [
                    {
                        "id": answer.id,
                        "text": answer.text,
                        "feedback": answer.feedback,
                    }
                    for answer in q.answers.filter(
                        id__in=filter_answers(self.answers, q.id)[0]["answers"]
                    )
                ],
            }
            for q in a.questions.all()
        ]

        self.feedback = feedback
        self.grade = (
            len(list(filter(lambda q: q["is_correct"], feedback)))
            / self.assignment.questions.count()
            * 100
        )

        return self
