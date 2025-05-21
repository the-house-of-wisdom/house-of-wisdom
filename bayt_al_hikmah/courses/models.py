"""Data Models for bayt_al_hikmah.courses"""

from django.db import models
from django.contrib.auth import get_user_model
from wagtail.fields import StreamField

from bayt_al_hikmah.cms.blocks import TextContentBlock
from bayt_al_hikmah.mixins.models import DateTimeMixin


# Create your models here.
User = get_user_model()


class Course(DateTimeMixin, models.Model):
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
    description = StreamField(
        TextContentBlock(),
        help_text="Item content",
    )
    tags = models.ManyToManyField(
        "tags.Tag",
        help_text="Course tags",
    )
    students = models.ManyToManyField(
        User,
        related_name="students",
        through="enrollments.Enrollment",
        help_text="Course enrollments",
    )

    @property
    def rating(self) -> float:
        """Course rating"""

        return 5.0

    @property
    def student_count(self) -> int:
        """Number of students enrolled in a course"""

        return self.students.count()

    def __str__(self) -> str:
        return self.name
