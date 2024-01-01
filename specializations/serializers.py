""" Serializers for learn.specializations """


from rest_framework.serializers import HyperlinkedModelSerializer
from learn.specializations.models import Specialization


# Create your serializers here.
class SpecializationSerializer(HyperlinkedModelSerializer):
    """Specialization serializer"""

    class Meta:
        """Meta data"""

        model = Specialization
        fields = [
            "id",
            "url",
        ]
