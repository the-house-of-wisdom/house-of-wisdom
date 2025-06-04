"""Serializers for how.posts"""

from rest_framework.serializers import ModelSerializer

from how.posts.models import Post


# Create your serializers here.
class PostSerializer(ModelSerializer):
    """Post serializer"""

    class Meta:
        """Meta data"""

        model = Post
        read_only_fields = ["owner", "course"]
        fields = [
            "id",
            "url",
            "owner",
            "course",
            "type",
            "content",
            "created_at",
            "updated_at",
        ]
