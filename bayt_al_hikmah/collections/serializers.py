"""Serializers for bayt_al_hikmah.collections"""

from rest_framework.serializers import ModelSerializer

from bayt_al_hikmah.collections.models import Collection


# Create your serializers here.
class CollectionSerializer(ModelSerializer):
    """Collection serializer"""

    class Meta:
        """Meta data"""

        model = Collection
        read_only_fields = ["user"]
        fields = [
            "id",
            "url",
            "user",
            "category",
            "enrollment_count",
            "image",
            "name",
            "headline",
            "description",
            "created_at",
            "updated_at",
            "tags",
        ]
