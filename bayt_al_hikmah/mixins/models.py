"""Model Mixins"""

from django.db import models


# Create your model mixins here.
class DateTimeMixin(models.Model):
    """Adds `created_at` and `updated_at` fields to a model"""

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

        abstract = True
