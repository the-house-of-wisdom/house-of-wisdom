""" Serializers for learn.courses """

from rest_framework.serializers import ModelSerializer
from learn.courses.models import Course


# Create your serializers here.
class CourseSerializer(ModelSerializer):
    """Course serializer"""

    class Meta:
        """Meta data"""

        model = Course
        read_only_fields = ["instructor"]
        fields = [
            "id",
            "url",
            "instructor",
            "image",
            "name",
            "headline",
            "description",
            "is_approved",
            "created_at",
            "updated_at",
        ]
