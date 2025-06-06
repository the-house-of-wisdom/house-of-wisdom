"""Serializers for how.questions"""

from rest_framework.serializers import ModelSerializer

from how.questions.models import Question


# Create your serializers here.
class QuestionSerializer(ModelSerializer):
    """Question serializer"""

    class Meta:
        """Meta data"""

        model = Question
        read_only_fields = ["assignment"]
        fields = [
            "id",
            "url",
            "assignment",
            "type",
            "text",
            "order",
            "created_at",
            "updated_at",
        ]
