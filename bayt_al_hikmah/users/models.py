"""Data Models for bayt_al_hikmah.users"""

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """Users"""

    is_instructor = models.BooleanField(
        null=True,
        blank=True,
        help_text="Designates weather the user is an instructor",
    )
    photo = models.ImageField(
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
    saved = models.ManyToManyField(
        "paths.Path",
        related_name="savers",
        help_text="Saved learning paths",
    )
    # NOTE: When generating migrations, you need to comment this field
    # generate the migrations then uncomment it to add it to Item model
    # to avoid django.db.migrations.exceptions.CircularDependencyError
    # items = models.ManyToManyField(
    #     "items.Item",
    #     related_name="completers",
    #     help_text="Completed items",
    # )
