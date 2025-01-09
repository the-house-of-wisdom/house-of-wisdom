""" Serializers for bayt_al_hikmah.items """

from rest_framework.serializers import ModelSerializer

from bayt_al_hikmah.items.models import Item


# Create your serializers here.
class ItemSerializer(ModelSerializer):
    """Item serializer"""

    class Meta:
        """Meta data"""

        model = Item
        fields = [
            "id",
            "url",
            "lesson",
            "type",
            "title",
            "description",
            "content",
            "file",
            "created_at",
            "updated_at",
        ]
