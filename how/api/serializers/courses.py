"""Serializers for how.apps.courses"""

from rest_framework.serializers import ModelSerializer

from how.apps.courses.models import Course


# Create your serializers here.
class CourseSerializer(ModelSerializer):
    """Course serializer"""

    class Meta:
        """Meta data"""

        model = Course
        read_only_fields = ["owner", "rating"]
        fields = [
            "id",
            "url",
            "owner",
            "image",
            "title",
            "rating",
            "headline",
            "description",
            "student_count",
            "created_at",
            "updated_at",
        ]
