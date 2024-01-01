""" Serializers for learn.projects """


from rest_framework.serializers import HyperlinkedModelSerializer
from learn.projects.models import Project


# Create your serializers here.
class ProjectSerializer(HyperlinkedModelSerializer):
    """Project serializer"""

    class Meta:
        """Meta data"""

        model = Project
        fields = [
            "id",
            "url",
        ]
