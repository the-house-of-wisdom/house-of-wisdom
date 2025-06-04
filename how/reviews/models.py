"""Data Models for how.reviews"""

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from how.mixins.models import DateTimeMixin
from how.reviews import RATINGS


# Create your models here.
User = get_user_model()


class Review(DateTimeMixin, models.Model):
    """Course Reviews"""

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews",
        help_text=_("Reviewer"),
    )
    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="reviews",
        help_text=_("Reviewed course"),
    )
    rating = models.PositiveSmallIntegerField(
        default=1,
        choices=RATINGS,
        help_text=_("Review rating"),
    )
    comment = models.CharField(
        max_length=512,
        db_index=True,
        help_text=_("Review comment"),
    )
    sentiment = models.BooleanField(
        null=True,
        blank=True,
        help_text=_("Review sentiment"),
    )

    class Meta:
        """Meta data"""

        constraints = [
            models.UniqueConstraint(name="unique_review", fields=["owner", "course"])
        ]

    def __str__(self) -> str:
        return f"{self.owner}: {self.course}-{self.rating}"
