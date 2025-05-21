"""API endpoints for bayt_al_hikmah.enrollments"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.enrollments.models import Enrollment
from bayt_al_hikmah.enrollments.serializers import EnrollmentSerializer
from bayt_al_hikmah.mixins.views import ActionPermDictMixin, UserFilterMixin
from bayt_al_hikmah.permissions import DenyAll, IsOwner


# Create your views here.
class BaseEnrollmentVS(ActionPermDictMixin, UserFilterMixin, ModelViewSet):
    """Base ViewSet for extension"""

    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    search_fields = ["course", "user"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["user", "course", "role"]
    action_perm_dict = {"default": permission_classes}


class EnrollmentViewSet(BaseEnrollmentVS):
    """View, update and delete Enrollments"""

    action_perm_dict = {**BaseEnrollmentVS.action_perm_dict, "create": [DenyAll]}


class CourseEnrollmentsVS(BaseEnrollmentVS):
    """Create, view, update and delete Course Enrollments"""

    def perform_create(self, serializer):
        """Add course to enrollment automatically"""

        serializer.save(
            user_id=self.request.user.pk, course_id=self.kwargs["course_id"]
        )

    def get_queryset(self):
        """Filter queryset by course"""

        return super().get_queryset().filter(course_id=self.kwargs["course_id"])
