"""Data Models for bayt_al_hikmah.enrollments"""

from django.core import validators
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from bayt_al_hikmah.enrollments import ENROLLMENT_ROLES
from bayt_al_hikmah.mixins.models import DateTimeMixin


# Create your models here.
User = get_user_model()


class Enrollment(DateTimeMixin, models.Model):
    """Course Enrollments"""

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="enrollments",
        help_text=_("Enrolling User"),
    )
    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="enrollments",
        help_text=_("Enrolled Course"),
    )
    role = models.PositiveSmallIntegerField(
        default=0,
        choices=ENROLLMENT_ROLES,
        help_text=_("Enrollment role"),
    )
    progress = models.FloatField(
        null=True,
        blank=True,
        help_text=_("Course completion progress"),
        validators=[
            validators.MinValueValidator(0.0, "Progress must be >= 0."),
            validators.MaxValueValidator(100.0, "Progress must be <= 100."),
        ],
    )
    is_completed = models.BooleanField(
        default=False,
        help_text=_("Designates weather the course is completed or not"),
    )

    class Meta:
        """Meta data"""

        constraints = [
            models.UniqueConstraint(
                name="unique_course_enrollment",
                fields=["owner", "course"],
            )
        ]

    def __str__(self) -> str:
        return f"{self.owner}-{self.course}-{ENROLLMENT_ROLES[self.role][1]}"
