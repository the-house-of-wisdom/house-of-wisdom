"""Serializers for how.apps.paths"""

from rest_framework.serializers import ModelSerializer

from how.apps.paths.models import LearningPath


# Create your serializers here.
class PathSerializer(ModelSerializer):
    """Path serializer"""

    class Meta:
        """Meta data"""

        model = LearningPath
        read_only_fields = ["owner", "rating"]
        fields = [
            "id",
            "url",
            "owner",
            "image",
            "title",
            "headline",
            "description",
            "created_at",
            "updated_at",
        ]
