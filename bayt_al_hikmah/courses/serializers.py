"""Serializers for bayt_al_hikmah.courses"""

from rest_framework.serializers import ModelSerializer

from bayt_al_hikmah.courses.models import Course


# Create your serializers here.
class CourseSerializer(ModelSerializer):
    """Course serializer"""

    class Meta:
        """Meta data"""

        model = Course
        read_only_fields = ["user"]
        fields = [
            "id",
            "url",
            "user",
            "category",
            "department",
            "specialization",
            "enrollment_count",
            "image",
            "name",
            "rating",
            "headline",
            "description",
            "created_at",
            "updated_at",
            "tags",
        ]
