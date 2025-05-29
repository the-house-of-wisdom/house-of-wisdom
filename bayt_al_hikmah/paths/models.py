"""Data Models for bayt_al_hikmah.paths"""

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from wagtail.fields import StreamField

from bayt_al_hikmah.mixins.models import DateTimeMixin
from bayt_al_hikmah.ui.cms.blocks import TextContentBlock


# Create your models here.
User = get_user_model()


class Path(DateTimeMixin, models.Model):
    """Learning Paths, Paths of related courses"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="paths",
        help_text=_("Learning Path instructor"),
    )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        related_name="paths",
        help_text=_("Learning Path category"),
    )
    image = models.ImageField(
        help_text=_("Learning Path image"),
        upload_to="images/paths/",
    )
    name = models.CharField(
        max_length=64,
        db_index=True,
        help_text=_("Learning Path name"),
    )
    headline = models.CharField(
        max_length=128,
        db_index=True,
        help_text=_("Learning Path headline"),
    )
    description = StreamField(
        TextContentBlock(),
        help_text=_("Learning Path description"),
    )
    prerequisites = StreamField(
        TextContentBlock(),
        null=True,
        blank=True,
        help_text=_("Learning Path prerequisites"),
    )
    duration = models.DurationField(
        null=True,
        blank=True,
        help_text=_("Learning Path duration"),
    )
    rating = models.FloatField(
        null=True,
        blank=True,
        db_index=True,
        help_text=_("Learning Path rating"),
    )
    tags = models.ManyToManyField(
        "tags.Tag",
        help_text=_("Learning Path tags"),
    )
    courses = models.ManyToManyField(
        "courses.Course",
        blank=True,
        help_text=_("Learning Path Courses"),
    )

    class Meta:
        """Meta data"""

        verbose_name = "Learning path"

    def __str__(self) -> str:
        return self.name
