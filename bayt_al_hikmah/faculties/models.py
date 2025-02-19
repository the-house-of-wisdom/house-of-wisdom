"""Data Models for bayt_al_hikmah.faculties"""

from django.db import models


# Create your models here.
class Faculty(models.Model):
    """Faculties"""

    image = models.ImageField(
        help_text="Faculty image",
        upload_to="images/faculties/",
    )
    name = models.CharField(
        max_length=64,
        db_index=True,
        help_text="Faculty name",
    )
    headline = models.CharField(
        max_length=128,
        db_index=True,
        help_text="Faculty headline",
    )
    description = models.TextField(
        help_text="Faculty description",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )

    class Meta:
        """Meta data"""

        verbose_name_plural = "faculties"

    def __str__(self) -> str:
        return self.name
