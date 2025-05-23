"""Serializers for bayt_al_hikmah.assignments"""

from rest_framework.serializers import ModelSerializer

from bayt_al_hikmah.assignments.models import Assignment


# Create your serializers here.
class AssignmentSerializer(ModelSerializer):
    """Assignment serializer"""

    class Meta:
        """Meta data"""

        model = Assignment
        read_only_fields = ["lesson"]
        fields = [
            "id",
            "url",
            "lesson",
            "title",
            "description",
            "question_count",
            "min_percentage",
            "content",
            "is_auto_graded",
            "created_at",
            "updated_at",
        ]
