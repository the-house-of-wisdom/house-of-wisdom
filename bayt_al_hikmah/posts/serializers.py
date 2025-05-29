"""Serializers for bayt_al_hikmah.posts"""

from rest_framework.serializers import ModelSerializer

from bayt_al_hikmah.posts.models import Post


# Create your serializers here.
class PostSerializer(ModelSerializer):
    """Post serializer"""

    class Meta:
        """Meta data"""

        model = Post
        read_only_fields = ["user", "course"]
        fields = [
            "id",
            "url",
            "user",
            "course",
            "type",
            "content",
            "created_at",
            "updated_at",
        ]
