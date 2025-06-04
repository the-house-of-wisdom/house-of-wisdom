"""Serializers for how.enrollments"""

from rest_framework.serializers import ModelSerializer

from how.enrollments.models import Enrollment


# Create your serializers here.
class EnrollmentSerializer(ModelSerializer):
    """Enrollment serializer"""

    class Meta:
        """Meta data"""

        model = Enrollment
        read_only_fields = [
            "owner",
            "course",
            "role",
            "progress",
            "is_completed",
        ]
        fields = [
            "id",
            "url",
            "owner",
            "course",
            "role",
            "progress",
            "is_completed",
            "created_at",
            "updated_at",
        ]
