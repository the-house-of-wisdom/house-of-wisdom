""" Data Models for learn.items """


from django.db import models
from django.core.serializers.json import DjangoJSONEncoder


# Create your models here.
class Item(models.Model):
    """Course Items"""

    module = models.ForeignKey(
        "modules.Module",
        on_delete=models.CASCADE,
        help_text="Item modules",
    )
    title = models.CharField(
        max_length=64,
        help_text="Item title",
    )
    content = models.JSONField(
        encoder=DjangoJSONEncoder,
        help_text="Item content",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Date created",
    )
