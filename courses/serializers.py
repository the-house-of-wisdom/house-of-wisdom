""" Serializers for learn.courses """


from rest_framework.serializers import HyperlinkedModelSerializer
from learn.courses.models import Course


# Create your serializers here.
class CourseSerializer(HyperlinkedModelSerializer):
    """Course serializer"""

    class Meta:
        """Meta data"""

        model = Course
        fields = [
            "id",
            "url",
        ]
