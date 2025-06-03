"""Serializers for bayt_al_hikmah.categories"""

from rest_framework.serializers import ModelSerializer

from bayt_al_hikmah.categories.models import Category


# Create your serializers here.
class CategorySerializer(ModelSerializer):
    """Category serializer"""

    class Meta:
        """Meta data"""

        model = Category
        fields = [
            "id",
            "url",
            "title",
            "description",
            "created_at",
            "updated_at",
        ]
