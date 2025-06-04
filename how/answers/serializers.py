"""Serializers for how.answers"""

from rest_framework.serializers import ModelSerializer

from how.answers.models import Answer


# Create your serializers here.
class AnswerSerializer(ModelSerializer):
    """Answer serializer"""

    class Meta:
        """Meta data"""

        model = Answer
        fields = [
            "id",
            "url",
            "is_correct",
            "text",
            "description",
            "created_at",
            "updated_at",
        ]
