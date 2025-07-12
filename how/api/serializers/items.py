"""Serializers for how.apps.items"""

from rest_framework.serializers import ModelSerializer

from how.apps.items.models import Item


# Create your serializers here.
class ItemSerializer(ModelSerializer):
    """Item serializer"""

    class Meta:
        """Meta data"""

        model = Item
        fields = [
            "id",
            "url",
            "type",
            "title",
            "content",
            "created_at",
            "updated_at",
        ]
