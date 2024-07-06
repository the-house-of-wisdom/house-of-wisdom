""" Data Models for learn.specializations """

from django.db import models


# Create your models here.
class Specialization(models.Model):
    """Specializations, collections of related courses"""

    instructor = models.ForeignKey(
        "instructors.Instructor",
        on_delete=models.CASCADE,
        help_text="Specialization Instructor",
    )
    image = models.ImageField(
        help_text="Specialization image",
        upload_to="images/specializations/",
    )
    name = models.CharField(
        max_length=64,
        unique=True,
        db_index=True,
        help_text="Specialization name",
    )
    headline = models.CharField(
        max_length=128,
        db_index=True,
        help_text="Specialization headline",
    )
    description = models.CharField(
        max_length=256,
        db_index=True,
        help_text="Specialization description",
    )
    is_approved = models.BooleanField(
        default=False,
        help_text="Designates if the specialization is approved by Learn.ai",
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
