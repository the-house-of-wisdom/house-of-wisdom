"""Serializers for how.apps.modules"""

from rest_framework.serializers import ModelSerializer

from how.apps.modules.models import Module


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
            "created_at",
            "updated_at",
        ]
