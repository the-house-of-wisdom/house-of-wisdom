"""Serializers for bayt_al_hikmah.courses"""

from rest_framework.serializers import ModelSerializer

from bayt_al_hikmah.courses.models import Course


# Create your serializers here.
class CourseSerializer(ModelSerializer):
    """Course serializer"""

    class Meta:
        """Meta data"""

        model = Course
        read_only_fields = ["user", "rating"]
        fields = [
            "id",
            "url",
            "user",
            "category",
            "image",
            "name",
            "rating",
            "headline",
            "description",
            "student_count",
            "created_at",
            "updated_at",
            "tags",
        ]
