"""Data Models for bayt_al_hikmah.submissions"""

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Submission(models.Model):
    """Assignment Submissions"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="submissions",
        help_text="User",
    )
    assignment = models.ForeignKey(
        "assignments.Assignment",
        on_delete=models.CASCADE,
        related_name="submissions",
        help_text="Submission assignment",
    )
    grade = models.FloatField(
        null=True,
        blank=True,
        help_text="Submission grade",
    )
    text = models.JSONField(
        null=True,
        blank=True,
        help_text="Submission payload",
    )
    file = models.FileField(
        null=True,
        blank=True,
        upload_to="files/submissions/",
        help_text="Submission file",
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to="files/images/",
        help_text="Submission image",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
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
