"""Data Models for bayt_al_hikmah.paths"""

from django.db import models
from django.contrib.auth import get_user_model
from wagtail.fields import StreamField

from bayt_al_hikmah.cms.blocks import TextContentBlock
from bayt_al_hikmah.mixins import DateTimeMixin


# Create your models here.
User = get_user_model()


class Path(DateTimeMixin, models.Model):
    """Learning Paths, Paths of related courses"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="paths",
        help_text="Path instructor",
    )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        related_name="paths",
        help_text="Path category",
    )
    image = models.ImageField(
        help_text="Path image",
        upload_to="images/paths/",
    )
    name = models.CharField(
        max_length=64,
        db_index=True,
        help_text="Path name",
    )
    headline = models.CharField(
        max_length=128,
        db_index=True,
        help_text="Path headline",
    )
    description = StreamField(
        TextContentBlock(),
        help_text="Item content",
    )
    tags = models.ManyToManyField(
        "tags.Tag",
        help_text="Path tags",
    )
    courses = models.ManyToManyField(
        "courses.Course",
        help_text="Path Courses",
    )

    class Meta:
        """Meta data"""

        verbose_name = "Learning path"

    @property
    def rating(self) -> float:
        """
        Path rating
        """
        # TODO
        return 1.0

    def __str__(self) -> str:
        return self.name
