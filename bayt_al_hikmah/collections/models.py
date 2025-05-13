"""Data Models for bayt_al_hikmah.collections"""

from django.db import models
from django.contrib.auth import get_user_model

from bayt_al_hikmah.mixins import DateTimeMixin


# Create your models here.
User = get_user_model()


class Collection(DateTimeMixin, models.Model):
    """Collections of related courses"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="collections",
        help_text="Collection instructor",
    )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        related_name="collections",
        help_text="Collection category",
    )
    image = models.ImageField(
        help_text="Collection image",
        upload_to="images/collections/",
    )
    name = models.CharField(
        max_length=64,
        db_index=True,
        help_text="Collection name",
    )
    headline = models.CharField(
        max_length=128,
        db_index=True,
        help_text="Collection headline",
    )
    description = models.TextField(
        help_text="Collection description",
    )
    tags = models.ManyToManyField(
        "tags.Tag",
        help_text="Collection tags",
    )
    collection_enrollments = models.ManyToManyField(
        User,
        related_name="collection_students",
        through="enrollments.Enrollment",
        help_text="Collection enrollments",
    )

    @property
    def rating(self) -> float:
        """
        Collection rating
        """
        # TODO
        return 1.0

    @property
    def enrollment_count(self) -> int:
        """
        Number of enrollments of a Collection
        """

        return self.collection_enrollments.count()

    def __str__(self) -> str:
        return self.name
