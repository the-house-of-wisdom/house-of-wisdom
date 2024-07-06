""" Serializers for learn.items """

from rest_framework.serializers import ModelSerializer
from learn.items.models import Item


# Create your serializers here.
class ItemSerializer(ModelSerializer):
    """Item serializer"""

    class Meta:
        """Meta data"""

        model = Item
        read_only_fields = ["module"]
        fields = [
            "id",
            "url",
            "module",
            "title",
            "content",
            "created_at",
            "updated_at",
        ]
