""" Serializers for learn.modules """


from rest_framework.serializers import HyperlinkedModelSerializer
from learn.modules.models import Module


# Create your serializers here.
class ModuleSerializer(HyperlinkedModelSerializer):
    """Module serializer"""

    class Meta:
        """Meta data"""

        model = Module
        fields = [
            "id",
            "url",
        ]
