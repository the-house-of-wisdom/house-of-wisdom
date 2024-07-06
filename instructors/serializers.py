""" Serializers for learn.instructors """

from rest_framework.serializers import ModelSerializer
from learn.instructors.models import Instructor


# Create your serializers here.
class InstructorSerializer(ModelSerializer):
    """Instructor serializer"""

    class Meta:
        """Meta data"""

        model = Instructor
        read_only_fields = ["user"]
        fields = [
            "id",
            "url",
            "user",
            "image",
            "name",
            "description",
            "is_approved",
            "created_at",
            "updated_at",
        ]
