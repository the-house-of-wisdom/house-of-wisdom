""" Data Models for bayt_al_hikmah.courses """

from django.db import models


# Create your models here.
class Course(models.Model):
    """Courses"""

    path = models.ForeignKey(
        "paths.Path",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Course path",
    )
    image = models.ImageField(
        help_text="Course image",
        upload_to="images/courses/",
    )
    name = models.CharField(
        max_length=64,
        unique=True,
        db_index=True,
        help_text="Course name",
    )
    headline = models.CharField(
        max_length=128,
        db_index=True,
        help_text="Course headline",
    )
    description = models.CharField(
        max_length=256,
        db_index=True,
        help_text="Course description",
    )
    is_approved = models.BooleanField(
        default=False,
        help_text="Designates if the course is approved",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )

    def __str__(self) -> str:
        return self.name
