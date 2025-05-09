"""Mixins"""

from django.db import models


# Create your mixins here.
class OwnerMixin:
    """Add the owner of the object"""

    def perform_create(self, serializer):
        """Save the object with owner"""

        serializer.save(user=self.request.user)


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
