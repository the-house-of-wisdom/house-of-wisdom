""" Serializers for learn.projects """

from rest_framework.serializers import ModelSerializer
from learn.projects.models import Project


# Create your serializers here.
class ProjectSerializer(ModelSerializer):
    """Project serializer"""

    class Meta:
        """Meta data"""

        model = Project
        fields = [
            "id",
            "url",
        ]
