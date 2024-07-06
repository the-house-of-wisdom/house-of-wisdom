""" Serializers for learn.accomplishments """

from rest_framework.serializers import ModelSerializer
from learn.accomplishments.models import Accomplishment


# Create your serializers here.
class AccomplishmentSerializer(ModelSerializer):
    """Accomplishment serializer"""

    class Meta:
        """Meta data"""

        model = Accomplishment
        read_only_fields = ["specialization", "course", "item"]
        fields = [
            "id",
            "url",
            "specialization",
            "course",
            "item",
            "created_at",
            "updated_at",
        ]
