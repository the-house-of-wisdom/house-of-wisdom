"""Serializers for bayt_al_hikmah.submissions"""

from rest_framework.serializers import ModelSerializer

from bayt_al_hikmah.submissions.models import Submission


# Create your serializers here.
class SubmissionCreateSerializer(ModelSerializer):
    """Submission serializer for create action"""

    class Meta:
        """Meta data"""

        model = Submission
        read_only_fields = ["user", "assignment", "grade", "feedback"]
        fields = [
            "id",
            "url",
            "user",
            "assignment",
            "grade",
            "status",
            "file",
            "answers",
            "feedback",
            "created_at",
            "updated_at",
        ]


class SubmissionSerializer(SubmissionCreateSerializer):
    """Submission serializer"""

    class Meta(SubmissionCreateSerializer.Meta):
        """Meta data"""

        read_only_fields = SubmissionCreateSerializer.Meta.read_only_fields + [
            "file",
            "answers",
        ]
