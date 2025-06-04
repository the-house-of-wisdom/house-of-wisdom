"""Serializers for how.modules"""

from rest_framework.serializers import ModelSerializer

from how.modules.models import Module


# Create your serializers here.
class ModuleSerializer(ModelSerializer):
    """Module serializer"""

    class Meta:
        """Meta data"""

        model = Module
        fields = [
            "id",
            "url",
            "title",
            "description",
            "order",
            "created_at",
            "updated_at",
        ]
