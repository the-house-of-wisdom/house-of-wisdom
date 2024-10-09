""" Serializers for bayt_al_hikmah.specializations """

from rest_framework.serializers import ModelSerializer

from bayt_al_hikmah.paths.models import Path


# Create your serializers here.
class PathSerializer(ModelSerializer):
    """Specialization serializer"""

    class Meta:
        """Meta data"""

        model = Path
        read_only_fields = ["user", "is_approved"]
        fields = [
            "id",
            "url",
            "user",
            "image",
            "name",
            "headline",
            "description",
            "is_approved",
            "created_at",
            "updated_at",
        ]
