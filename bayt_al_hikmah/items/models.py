""" Data Models for bayt_al_hikmah.items """

from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.
class Item(models.Model):
    """Course Items"""

    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        help_text="Course",
    )
    module = models.ForeignKey(
        "modules.Module",
        on_delete=models.CASCADE,
        help_text="Module",
    )
    title = models.CharField(
        max_length=64,
        db_index=True,
        help_text="Title",
    )
    description = models.CharField(
        max_length=256,
        db_index=True,
        help_text="Description",
    )
    content = models.TextField(
        null=True,
        blank=True,
        help_text="Content",
    )
    file = models.FileField(
        null=True,
        blank=True,
        help_text="Upload a file",
        upload_to="files/items/",
        validators=[
            FileExtensionValidator(
                allowed_extensions=["zip", "mp4", "pdf", "docx", "ppt"]
            )
        ],
    )
    type = models.PositiveSmallIntegerField(
        help_text="Type",
        choices=[
            (1, "Video"),
            (2, "Reading"),
            (3, "Quiz"),
            (4, "Assignment"),
        ],
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
        return super().__str__()
