"""Data Models for bayt_al_hikmah.posts"""

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from wagtail.fields import StreamField

from bayt_al_hikmah.cms.blocks import CommonContentBlock
from bayt_al_hikmah.mixins.models import DateTimeMixin


# Create your models here.
User = get_user_model()


class Post(DateTimeMixin, models.Model):
    """Course Posts"""

    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="posts",
        help_text=_("Post owner"),
    )
    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.PROTECT,
        related_name="posts",
        help_text=_("Post course"),
    )
    title = models.CharField(
        max_length=64,
        db_index=True,
        help_text=_("Post title"),
    )
    content = StreamField(
        CommonContentBlock(),
        help_text=_("Post content"),
    )

    def __str__(self) -> str:
        return f"{self.course}"
