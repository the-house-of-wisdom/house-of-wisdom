"""Data Models for bayt_al_hikmah.paths"""

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from wagtail.fields import StreamField

from bayt_al_hikmah.cms.blocks import TextContentBlock
from bayt_al_hikmah.mixins.models import DateTimeMixin


# Create your models here.
User = get_user_model()


class Path(DateTimeMixin, models.Model):
    """Learning Paths, Paths of related courses"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="paths",
        help_text=_("Path instructor"),
    )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        related_name="paths",
        help_text=_("Path category"),
    )
    image = models.ImageField(
        help_text=_("Path image"),
        upload_to="images/paths/",
    )
    name = models.CharField(
        max_length=64,
        db_index=True,
        help_text=_("Path name"),
    )
    headline = models.CharField(
        max_length=128,
        db_index=True,
        help_text=_("Path headline"),
    )
    description = StreamField(
        TextContentBlock(),
        help_text=_("Path description"),
    )
    rating = models.FloatField(
        null=True,
        blank=True,
        db_index=True,
        help_text=_("Path rating"),
    )
    tags = models.ManyToManyField(
        "tags.Tag",
        help_text=_("Path tags"),
    )
    courses = models.ManyToManyField(
        "courses.Course",
        blank=True,
        help_text=_("Path Courses"),
    )

    class Meta:
        """Meta data"""

        verbose_name = "Learning path"

    def __str__(self) -> str:
        return self.name
