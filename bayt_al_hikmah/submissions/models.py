"""Data Models for bayt_al_hikmah.submissions"""

from django.db import models
from django.core import validators
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from bayt_al_hikmah.mixins.models import DateTimeMixin


# Create your models here.
User = get_user_model()


class Submission(DateTimeMixin, models.Model):
    """Assignment Submissions"""

    user = models.ForeignKey(
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

    def status(self) -> str:
        """Submission status"""

        return (
            "Pending"
            if self.grade is None
            else "Passed" if self.grade >= self.assignment.min_percentage else "Failed"
        )

    def __str__(self) -> str:
        return f"{self.assignment}: Submission {self.pk}"
