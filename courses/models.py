""" Data Models for learn.courses """


from django.db import models


# Create your models here.
class Course(models.Model):
    """Courses"""

    specialization = models.ForeignKey(
        "specialization.Specialization",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Course specialization",
    )
    image = models.ImageField(
        help_text="Specialization image",
        upload_to="images/specializations/",
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
        help_text="Designates if the course is approved by LearnLMS",
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
