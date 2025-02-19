"""Serializers for bayt_al_hikmah.reviews"""

from rest_framework.serializers import ModelSerializer

from bayt_al_hikmah.reviews.models import Review


# Create your serializers here.
class ReviewSerializer(ModelSerializer):
    """Review serializer"""

    class Meta:
        """Meta data"""

        model = Review
        read_only_fields = ["user", "course"]
        fields = [
            "id",
            "url",
            "user",
            "course",
            "rating",
            "comment",
            "sentiment",
            "created_at",
            "updated_at",
        ]
