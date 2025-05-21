"""Model Mixins"""

from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your model mixins here.
class DateTimeMixin(models.Model):
    """Adds `created_at` and `updated_at` fields to a model"""

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text=_("Date created"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text=_("Last update"),
    )

    class Meta:
        """Meta data"""

        abstract = True
