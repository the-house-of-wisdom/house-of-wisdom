"""Serializers for bayt_al_hikmah.submissions"""

from rest_framework.serializers import ModelSerializer

from bayt_al_hikmah.submissions.models import Submission


# Create your serializers here.
class SubmissionSerializer(ModelSerializer):
    """Submission serializer"""

    class Meta:
        """Meta data"""

        model = Submission
        read_only_fields = ["user", "assignment"]
        fields = [
            "id",
            "url",
            "user",
            "assignment",
            "status",
            "grade",
            "text",
            "file",
            "image",
            "created_at",
            "updated_at",
        ]
