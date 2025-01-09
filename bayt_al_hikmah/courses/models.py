""" Data Models for bayt_al_hikmah.courses """

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Course(models.Model):
    """Courses"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="courses",
        help_text="Course instructor",
    )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        related_name="courses",
        help_text="Course category",
    )
    department = models.ForeignKey(
        "departments.Department",
        on_delete=models.CASCADE,
        related_name="courses",
        help_text="Course department",
    )
    specialization = models.ForeignKey(
        "specializations.Specialization",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Course specialization",
    )
    image = models.ImageField(
        help_text="Course image",
        upload_to=" images/courses/",
    )
    name = models.CharField(
        max_length=64,
        db_index=True,
        help_text="Course name",
    )
    headline = models.CharField(
        max_length=128,
        db_index=True,
        help_text="Course headline",
    )
    description = models.TextField(
        help_text="Course description",
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
        help_text="Course tags",
    )
    course_enrollments = models.ManyToManyField(
        User,
        related_name="course_students",
        through="enrollments.Enrollment",
        help_text="Course enrollments",
    )

    @property
    def rating(self) -> float:
        """
        Course rating
        """

        # TODO
        return 1.0

    @property
    def enrollment_count(self) -> int:
        """
        Number of enrollments of a course
        """

        return self.course_enrollments.count()

    def __str__(self) -> str:
        return self.name
