"""Serializers for how.apps.submissions"""

from rest_framework.serializers import ModelSerializer

from how.apps.submissions.models import Submission


# Create your serializers here.
class SubmissionCreateSerializer(ModelSerializer):
    """Submission serializer for create action"""

    class Meta:
        """Meta data"""

        model = Submission
        read_only_fields = ["owner", "assignment", "grade", "feedback"]
        fields = [
            "id",
            "url",
            "owner",
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
