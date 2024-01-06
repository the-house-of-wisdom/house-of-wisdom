""" Data Models for learn.enrollments """


from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Enrollment(models.Model):
    """Enrollments"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="Completer",
    )
    specialization = models.ForeignKey(
        "specializations.Specialization",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Completed Specialization",
    )
    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Completed Course",
    )
    is_approved = models.BooleanField(
        default=False,
        help_text="Designate if the enrollment is approved by LearnLMS",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Last update",
    )

    class Meta:
        """Meta data"""

        constraints = [
            models.UniqueConstraint(
                name="unique_enrollment_user_specialization",
                fields=["user", "specialization"],
            ),
            models.UniqueConstraint(
                name="unique_enrollment_user_course",
                fields=["user", "course"],
            ),
        ]

    def __str__(self) -> str:
        completed = (
            self.specialization if self.specialization is not None else self.course
        )
        return f"{self.user}, {completed}"
