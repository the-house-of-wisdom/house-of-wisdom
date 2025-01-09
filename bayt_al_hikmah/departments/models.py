""" Data Models for bayt_al_hikmah.departments """

from django.db import models


# Create your models here.
class Department(models.Model):
    """Departments"""

    faculty = models.ForeignKey(
        "faculties.Faculty",
        on_delete=models.CASCADE,
        related_name="departments",
        help_text="Department faculty",
    )
    image = models.ImageField(
        help_text="Department image",
        upload_to="images/departments/",
    )
    name = models.CharField(
        max_length=64,
        db_index=True,
        help_text="Department name",
    )
    headline = models.CharField(
        max_length=128,
        db_index=True,
        help_text="Department headline",
    )
    description = models.TextField(
        help_text="Department description",
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
