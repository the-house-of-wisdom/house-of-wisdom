""" Data Models for learn """


from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """Learn Users"""

    image = models.ImageField(
        help_text="Profile image",
        upload_to="images/users/",
    )
    bio = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text="Tell us about yourself",
    )
    specializations = models.ManyToManyField(
        "specializations.Specialization",
        through="enrollments.Enrollment",
        help_text="Enrolled specializations",
    )
    courses = models.ManyToManyField(
        "courses.Course",
        through="enrollments.Enrollment",
        help_text="Enrolled courses",
    )
