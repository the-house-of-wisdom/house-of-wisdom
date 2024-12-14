""" Serializers for bayt_al_hikmah.courses """

from rest_framework.serializers import ModelSerializer

from bayt_al_hikmah.courses.models import Course


# Create your serializers here.
class CourseSerializer(ModelSerializer):
    """Course serializer"""

    class Meta:
        """Meta data"""

        model = Course
        read_only_fields = ["institute", "is_approved"]
        fields = [
            "id",
            "url",
            "institute",
            "instructors",
            "image",
            "name",
            "headline",
            "description",
            "is_approved",
            "created_at",
            "updated_at",
        ]
