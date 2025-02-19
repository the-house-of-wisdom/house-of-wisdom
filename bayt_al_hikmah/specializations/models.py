"""Data Models for bayt_al_hikmah.specializations"""

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Specialization(models.Model):
    """Specializations, collections of related courses"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="specializations",
        help_text="Specialization instructor",
    )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        related_name="specializations",
        help_text="Specialization category",
    )
    department = models.ForeignKey(
        "departments.Department",
        on_delete=models.CASCADE,
        related_name="specializations",
        help_text="Specialization department",
    )
    image = models.ImageField(
        help_text="Specialization image",
        upload_to="images/specializations/",
    )
    name = models.CharField(
        max_length=64,
        db_index=True,
        help_text="Specialization name",
    )
    headline = models.CharField(
        max_length=128,
        db_index=True,
        help_text="Specialization headline",
    )
    description = models.TextField(
        help_text="Specialization description",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )
    tags = models.ManyToManyField(
        "tags.Tag",
        help_text="Specialization tags",
    )
    specialization_enrollments = models.ManyToManyField(
        User,
        related_name="specialization_students",
        through="enrollments.Enrollment",
        help_text="Specialization enrollments",
    )

    @property
    def rating(self) -> float:
        """
        Specialization rating
        """
        # TODO
        return 1.0

    @property
    def enrollment_count(self) -> int:
        """
        Number of enrollments of a Specialization
        """

        return self.specialization_enrollments.count()

    def __str__(self) -> str:
        return self.name
