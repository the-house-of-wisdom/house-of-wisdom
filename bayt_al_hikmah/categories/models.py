"""Data Models for bayt_al_hikmah.categories"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.fields import StreamField

from bayt_al_hikmah.mixins.models import DateTimeMixin
from bayt_al_hikmah.ui.cms.blocks import TextContentBlock


# Create your models here.
class Category(DateTimeMixin, models.Model):
    """Categories"""

    name = models.CharField(
        max_length=64,
        unique=True,
        db_index=True,
        help_text=_("Category name"),
    )
    description = StreamField(
        TextContentBlock(),
        help_text=_("Category description"),
    )

    class Meta:
        """Meta data"""

        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.name
