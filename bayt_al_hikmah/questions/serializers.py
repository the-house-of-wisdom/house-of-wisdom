"""Serializers for bayt_al_hikmah.questions"""

from rest_framework.serializers import ModelSerializer

from bayt_al_hikmah.questions.models import Question


# Create your serializers here.
class QuestionSerializer(ModelSerializer):
    """Question serializer"""

    class Meta:
        """Meta data"""

        model = Question
        fields = [
            "id",
            "url",
            "type",
            "text",
            "order",
            "created_at",
            "updated_at",
        ]
