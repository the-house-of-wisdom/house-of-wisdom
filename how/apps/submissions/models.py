"""Data Models for how.apps.submissions"""

from typing import Optional

from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _

from how.apps.mixins import DateTimeMixin

# Create your models here.
User = get_user_model()


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
    answers = models.ManyToManyField(
        "answers.Answer",
        blank=True,
        help_text=_("Submission answers"),
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

    def auto_grade(self) -> Optional[float]:
        """Auto grade the submission"""

        assignment = self.assignment

        # Check if the submission is auto graded
        if not assignment.is_auto_graded:
            return

        # Calculate the grade
        return (
            self.answers.filter(is_correct=True).count()
            / sum(
                q.answers.filter(is_correct=True).count()
                for q in assignment.questions.all()
            )
            * 100
        )
