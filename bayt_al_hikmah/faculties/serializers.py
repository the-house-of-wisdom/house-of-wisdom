"""Serializers for bayt_al_hikmah.faculties"""

from rest_framework.serializers import ModelSerializer

from bayt_al_hikmah.faculties.models import Faculty


# Create your serializers here.
class FacultySerializer(ModelSerializer):
    """Faculty serializer"""

    class Meta:
        """Meta data"""

        model = Faculty
        fields = [
            "id",
            "url",
            "image",
            "name",
            "headline",
            "description",
            "created_at",
            "updated_at",
        ]
