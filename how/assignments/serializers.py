"""Serializers for how.assignments"""

from rest_framework.serializers import ModelSerializer

from how.assignments.models import Assignment


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
            "question_count",
            "min_percentage",
            "content",
            "is_auto_graded",
            "order",
            "created_at",
            "updated_at",
        ]
