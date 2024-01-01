""" Serializers for learn.accomplishments """


from rest_framework.serializers import HyperlinkedModelSerializer
from learn.accomplishments.models import Accomplishment


# Create your serializers here.
class AccomplishmentSerializer(HyperlinkedModelSerializer):
    """Accomplishment serializer"""

    class Meta:
        """Meta data"""

        model = Accomplishment
        fields = [
            "id",
            "url",
        ]
