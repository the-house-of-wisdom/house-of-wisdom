""" Serializers for learn.specializations """

from rest_framework.serializers import ModelSerializer
from learn.specializations.models import Specialization


# Create your serializers here.
class SpecializationSerializer(ModelSerializer):
    """Specialization serializer"""

    class Meta:
        """Meta data"""

        model = Specialization
        read_only_fields = ["instructor"]
        fields = [
            "id",
            "url",
            "instructor",
            "image",
            "name",
            "headline",
            "description",
            "is_approved",
            "created_at",
            "updated_at",
        ]
