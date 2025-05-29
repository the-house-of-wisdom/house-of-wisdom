"""Data Models for bayt_al_hikmah.items"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.fields import StreamField

from bayt_al_hikmah.items import ITEM_TYPES
from bayt_al_hikmah.mixins.models import DateTimeMixin
from bayt_al_hikmah.ui.cms.blocks import CommonContentBlock


# Create your models here.
class Item(DateTimeMixin, models.Model):
    """Lesson Items"""

    lesson = models.ForeignKey(
        "lessons.Lesson",
        on_delete=models.PROTECT,
        related_name="items",
        help_text=_("Item lesson"),
    )
    title = models.CharField(
        max_length=64,
        db_index=True,
        help_text=_("Item title"),
    )
    type = models.PositiveSmallIntegerField(
        default=0,
        help_text=_("Item type"),
        choices=ITEM_TYPES,
    )
    content = StreamField(
        CommonContentBlock(),
        help_text=_("Item content"),
    )
    order = models.SmallIntegerField(
        default=0,
        help_text=_("Item order in the lesson"),
    )

    def __str__(self) -> str:
        return self.title
