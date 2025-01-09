""" Serializers for bayt_al_hikmah.answers """

from rest_framework.serializers import ModelSerializer

from bayt_al_hikmah.answers.models import Answer


# Create your serializers here.
class AnswerSerializer(ModelSerializer):
    """Answer serializer"""

    class Meta:
        """Meta data"""

        model = Answer
        fields = [
            "id",
            "url",
            "question",
            "is_correct",
            "text",
            "description",
            "created_at",
            "updated_at",
        ]
