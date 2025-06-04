"""Serializers for how.blog"""

from rest_framework.serializers import ModelSerializer

from how.blog.models import Article


# Create your serializers here.
class ArticleSerializer(ModelSerializer):
    """Blog serializer"""

    class Meta:
        """Meta data"""

        model = Article
        fields = [
            "id",
            "url",
            "title",
            "headline",
            "content",
            "created_at",
            "updated_at",
        ]
