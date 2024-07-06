""" Data Models for learn.instructors """

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Instructor(models.Model):
    """Instructors"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="Owner",
    )
    image = models.ImageField(
        help_text="Profile image",
        upload_to="images/instructors",
    )
    name = models.CharField(
        max_length=64,
        unique=True,
        db_index=True,
        help_text="Instructor name",
    )
    description = models.CharField(
        max_length=256,
        db_index=True,
        help_text="Instructor description",
    )
    is_approved = models.BooleanField(
        default=False,
        help_text="Designates if the instructor is approved by Learn.ai",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Date created",
    )

    def __str__(self) -> str:
        return self.name
