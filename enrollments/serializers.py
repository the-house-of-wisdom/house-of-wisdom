""" Serializers for learn.enrollments """

from rest_framework.serializers import ModelSerializer
from learn.enrollments.models import Enrollment


# Create your serializers here.
class EnrollmentSerializer(ModelSerializer):
    """Enrollment serializer"""

    class Meta:
        """Meta data"""

        model = Enrollment
        read_only_fields = ["specialization", "course", "is_approved"]
        fields = [
            "id",
            "url",
            "specialization",
            "course",
            "is_approved",
            "created_at",
            "updated_at",
        ]
