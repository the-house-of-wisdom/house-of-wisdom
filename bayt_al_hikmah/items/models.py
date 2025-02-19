"""Data Models for bayt_al_hikmah.items"""

from django.db import models
from django.core.validators import FileExtensionValidator

from bayt_al_hikmah.items import ITEM_TYPES


# Create your models here.
class Item(models.Model):
    """Lesson Items"""

    lesson = models.ForeignKey(
        "lessons.Lesson",
        on_delete=models.CASCADE,
        related_name="items",
        help_text="Item lesson",
    )
    title = models.CharField(
        max_length=64,
        db_index=True,
        help_text="Item title",
    )
    description = models.TextField(
        help_text="Item description",
    )
    content = models.TextField(
        null=True,
        blank=True,
        help_text="Item content",
    )
    file = models.FileField(
        null=True,
        blank=True,
        help_text="Item file",
        upload_to="files/items/",
        validators=[
            FileExtensionValidator(
                allowed_extensions=["zip", "mp4", "pdf", "docx", "ppt"]
            )
        ],
    )
    type = models.PositiveSmallIntegerField(
        default=0,
        help_text="Item type",
        choices=ITEM_TYPES,
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
        return self.title
