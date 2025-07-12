"""Serializers for how.apps.answers"""

from rest_framework.serializers import ModelSerializer

from how.apps.answers.models import Answer


# Create your serializers here.
class AnswerSerializer(ModelSerializer):
    """Answer serializer"""

    class Meta:
        """Meta data"""

        model = Answer
        read_only_fields = ["question"]
        fields = [
            "id",
            "url",
            "question",
            "is_correct",
            "text",
            "feedback",
            "created_at",
            "updated_at",
        ]
