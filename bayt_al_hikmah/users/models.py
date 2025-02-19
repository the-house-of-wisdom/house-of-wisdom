"""Data Models for bayt_al_hikmah.users"""

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """Users"""

    department = models.ForeignKey(
        "departments.Department",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="users",
        help_text="Department",
    )
    is_instructor = models.BooleanField(
        default=False,
        help_text="Designates weather the user is an instructor",
    )
    image = models.ImageField(
        null=True,
        blank=True,
        help_text="Profile image",
        upload_to="images/users/",
    )
    bio = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text="Tell us about yourself",
    )
