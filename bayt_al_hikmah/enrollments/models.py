"""Data Models for bayt_al_hikmah.enrollments"""

from django.db import models
from django.contrib.auth import get_user_model

from bayt_al_hikmah.enrollments import ENROLLMENT_ROLES
from bayt_al_hikmah.mixins import DateTimeMixin


# Create your models here.
User = get_user_model()


class Enrollment(DateTimeMixin, models.Model):
    """Course & Collection Enrollments"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="enrollments",
        help_text="Enrolling User",
    )
    collection = models.ForeignKey(
        "collections.Collection",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="enrollments",
        help_text="Enrolled Collection",
    )
    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="enrollments",
        help_text="Enrolled Course",
    )
    role = models.PositiveSmallIntegerField(
        default=0,
        choices=ENROLLMENT_ROLES,
        help_text="Enrollment role",
    )

    class Meta:
        """Meta data"""

        constraints = [
            models.UniqueConstraint(
                name="unique_course_enrollment",
                fields=["user", "course"],
            ),
            models.UniqueConstraint(
                name="unique_collection_enrollment",
                fields=["user", "collection"],
            ),
        ]

    def __str__(self) -> str:
        return f"{self.user}-{self.course if self.course else self.collection}"
