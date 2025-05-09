"""Serializers for bayt_al_hikmah.specializations"""

from rest_framework.serializers import ModelSerializer

from bayt_al_hikmah.specializations.models import Specialization


# Create your serializers here.
class SpecializationSerializer(ModelSerializer):
    """Specialization serializer"""

    class Meta:
        """Meta data"""

        model = Specialization
        read_only_fields = ["user"]
        fields = [
            "id",
            "url",
            "user",
            "category",
            "enrollment_count",
            "image",
            "name",
            "headline",
            "description",
            "created_at",
            "updated_at",
            "tags",
        ]
