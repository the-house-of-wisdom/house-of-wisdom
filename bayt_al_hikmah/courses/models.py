"""Data Models for bayt_al_hikmah.courses"""

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from wagtail.fields import StreamField

from bayt_al_hikmah.mixins.models import DateTimeMixin
from bayt_al_hikmah.ui.cms.blocks import CoursePrerequisitesBlock, TextContentBlock


# Create your models here.
User = get_user_model()


class Course(DateTimeMixin, models.Model):
    """Courses"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="courses",
        help_text=_("Course instructor"),
    )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        related_name="courses",
        help_text=_("Course category"),
    )
    image = models.ImageField(
        help_text=_("Course image"),
        upload_to=" images/courses/",
    )
    name = models.CharField(
        max_length=64,
        db_index=True,
        help_text=_("Course name"),
    )
    headline = models.CharField(
        max_length=128,
        db_index=True,
        help_text=_("Course headline"),
    )
    rating = models.FloatField(
        null=True,
        blank=True,
        db_index=True,
        help_text=_("Course rating"),
    )
    description = StreamField(
        TextContentBlock(),
        help_text=_("Course description"),
    )
    prerequisites = StreamField(
        CoursePrerequisitesBlock(),
        null=True,
        blank=True,
        help_text=_("Course prerequisites"),
    )
    duration = models.DurationField(
        null=True,
        blank=True,
        help_text=_("Course duration"),
    )
    tags = models.ManyToManyField(
        "tags.Tag",
        blank=True,
        help_text=_("Course tags"),
    )
    students = models.ManyToManyField(
        User,
        related_name="students",
        through="enrollments.Enrollment",
        help_text=_("Course enrollments"),
    )

    @property
    def student_count(self) -> int:
        """Number of students enrolled in a course"""

        return self.students.count()

    def __str__(self) -> str:
        return self.name
