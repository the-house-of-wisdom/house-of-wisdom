"""Serializers for bayt_al_hikmah.assignments"""

from rest_framework.serializers import ModelSerializer

from bayt_al_hikmah.assignments.models import Assignment


# Create your serializers here.
class AssignmentSerializer(ModelSerializer):
    """Assignment serializer"""

    class Meta:
        """Meta data"""

        model = Assignment
        fields = [
            "id",
            "url",
            "lesson",
            "is_auto_graded",
            "title",
            "description",
            "content",
            "created_at",
            "updated_at",
        ]
