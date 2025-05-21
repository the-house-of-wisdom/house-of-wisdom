"""Data Models for bayt_al_hikmah.items"""

from django.db import models
from wagtail.fields import StreamField


from bayt_al_hikmah.cms.blocks import CommonContentBlock
from bayt_al_hikmah.items import ITEM_TYPES
from bayt_al_hikmah.mixins.models import DateTimeMixin


# Create your models here.
class Item(DateTimeMixin, models.Model):
    """Lesson Items"""

    lesson = models.ForeignKey(
        "lessons.Lesson",
        on_delete=models.PROTECT,
        related_name="items",
        help_text="Item lesson",
    )
    title = models.CharField(
        max_length=64,
        db_index=True,
        help_text="Item title",
    )
    type = models.PositiveSmallIntegerField(
        default=0,
        help_text="Item type",
        choices=ITEM_TYPES,
    )
    content = StreamField(
        CommonContentBlock(),
        help_text="Item content",
    )

    def __str__(self) -> str:
        return self.title
