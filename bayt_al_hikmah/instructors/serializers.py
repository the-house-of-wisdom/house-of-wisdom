""" Serializers for bayt_al_hikmah.instructors """

from rest_framework.serializers import ModelSerializer

from bayt_al_hikmah.instructors.models import Instructor


# Create your serializers here.
class InstructorSerializer(ModelSerializer):
    """Specialization serializer"""

    class Meta:
        """Meta data"""

        model = Instructor
        read_only_fields = ["user", "is_approved"]
        fields = [
            "id",
            "url",
            "user",
            "institute",
            "is_approved",
            "created_at",
            "updated_at",
        ]
