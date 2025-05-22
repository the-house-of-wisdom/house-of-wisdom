"""Serializers for bayt_al_hikmah.blog"""

from rest_framework.serializers import ModelSerializer

from bayt_al_hikmah.blog.models import Blog


# Create your serializers here.
class BlogSerializer(ModelSerializer):
    """Blog serializer"""

    class Meta:
        """Meta data"""

        model = Blog
        fields = [
            "id",
            "url",
            "title",
            "headline",
            "content",
            "created_at",
            "updated_at",
        ]
