"""Serializers for bayt_al_hikmah.paths"""

from rest_framework.serializers import ModelSerializer

from bayt_al_hikmah.paths.models import Path


# Create your serializers here.
class PathSerializer(ModelSerializer):
    """Path serializer"""

    class Meta:
        """Meta data"""

        model = Path
        read_only_fields = ["user"]
        fields = [
            "id",
            "url",
            "user",
            "category",
            "image",
            "name",
            "headline",
            "description",
            "created_at",
            "updated_at",
            "courses",
            "tags",
        ]
