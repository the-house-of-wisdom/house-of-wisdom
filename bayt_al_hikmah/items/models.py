"""Data Models for bayt_al_hikmah.items"""

from django.db import models
from django.core.validators import FileExtensionValidator

from bayt_al_hikmah.items import ITEM_TYPES
from bayt_al_hikmah.mixins import DateTimeMixin


# Create your models here.
class Item(DateTimeMixin, models.Model):
    """Lesson Items"""

    lesson = models.ForeignKey(
        "lessons.Lesson",
        on_delete=models.CASCADE,
        related_name="items",
        help_text="Item lesson",
    )
    type = models.PositiveSmallIntegerField(
        default=0,
        help_text="Item type",
        choices=ITEM_TYPES,
    )
    title = models.CharField(
        max_length=64,
        db_index=True,
        help_text="Item title",
    )
    content = models.TextField(
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

    def __str__(self) -> str:
        return self.title
