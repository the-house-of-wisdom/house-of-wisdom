""" Serializers for learn.modules """


from rest_framework.serializers import ModelSerializer
from learn.modules.models import Module


# Create your serializers here.
class ModuleSerializer(ModelSerializer):
    """Module serializer"""

    class Meta:
        """Meta data"""

        model = Module
        read_only_fields = ["course"]
        fields = [
            "id",
            "url",
            "title",
            "description",
            "created_at",
            "updated_at",
        ]
