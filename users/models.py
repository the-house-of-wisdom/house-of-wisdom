""" Data Models for learn.users """

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    """Learn.ai Users"""

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
