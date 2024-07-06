""" Data Models for learn.accomplishments """

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Accomplishment(models.Model):
    """Accomplishments"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="Completer",
    )
    specialization = models.ForeignKey(
        "specializations.Specialization",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Completed Specialization",
    )
    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Completed Course",
    )
    item = models.ForeignKey(
        "items.Item",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Completed Item",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Last update",
    )

    class Meta:
        """Meta data"""

        constraints = [
            models.UniqueConstraint(
                name="unique_accomplishment_user_specialization",
                fields=["user", "specialization"],
            ),
            models.UniqueConstraint(
                name="unique_accomplishment_user_course",
                fields=["user", "course"],
            ),
            models.UniqueConstraint(
                name="unique_accomplishment_user_item",
                fields=["user", "item"],
            ),
        ]

    def __str__(self) -> str:
        completed = (
            self.specialization
            if self.specialization is not None
            else self.course if self.course is not None else self.item
        )
        return f"{self.user}, {completed}"
