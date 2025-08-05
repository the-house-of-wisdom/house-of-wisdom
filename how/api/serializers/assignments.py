"""Serializers for how.apps.assignments"""

from rest_framework.serializers import ModelSerializer

from how.apps.assignments.models import Assignment


# Create your serializers here.
class AssignmentSerializer(ModelSerializer):
    """Assignment serializer"""

    class Meta:
        """Meta data"""

        model = Assignment
        fields = [
            "id",
            "url",
            "title",
            "description",
            "content",
            "is_graded",
            "is_auto_graded",
            "question_count",
            "min_percentage",
            "created_at",
            "updated_at",
        ]
