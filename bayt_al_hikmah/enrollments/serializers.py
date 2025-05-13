"""Serializers for bayt_al_hikmah.enrollments"""

from rest_framework.serializers import ModelSerializer

from bayt_al_hikmah.enrollments.models import Enrollment


# Create your serializers here.
class EnrollmentSerializer(ModelSerializer):
    """Enrollment serializer"""

    class Meta:
        """Meta data"""

        model = Enrollment
        read_only_fields = ["user", "collection", "course", "role"]
        fields = [
            "id",
            "url",
            "user",
            "collection",
            "course",
            "role",
            "created_at",
            "updated_at",
        ]
