""" Data Models for bayt_al_hikmah.users """

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """bayt_al_hikmah.ai Users"""

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
