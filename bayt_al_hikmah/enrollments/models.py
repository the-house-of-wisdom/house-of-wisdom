""" Data Models for bayt_al_hikmah.enrollments """

from django.db import models
from django.contrib.auth import get_user_model

from bayt_al_hikmah.enrollments import ENROLLMENT_ROLES


# Create your models here.
User = get_user_model()


class Enrollment(models.Model):
    """Course & Specialization Enrollments"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="enrollments",
        help_text="Enrolling User",
    )
    specialization = models.ForeignKey(
        "specializations.Specialization",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="enrollments",
        help_text="Enrolled Specialization",
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
    is_approved = models.BooleanField(
        null=True,
        blank=True,
        help_text="Weather the enrollment is approved",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )

    class Meta:
        """Meta data"""

        constraints = [
            models.UniqueConstraint(
                name="unique_course_enrollment",
                fields=["user", "course"],
            ),
            models.UniqueConstraint(
                name="unique_specialization_enrollment",
                fields=["user", "specialization"],
            ),
        ]

    def __str__(self) -> str:
        status = (
            "Pending"
            if self.is_approved is None
            else "Approved" if self.is_approved else "Rejected"
        )

        return f"{self.user}-{self.course}: {status}"
