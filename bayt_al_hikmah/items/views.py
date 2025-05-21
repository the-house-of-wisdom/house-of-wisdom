"""API endpoints for bayt_al_hikmah.items"""

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from bayt_al_hikmah.items.models import Item
from bayt_al_hikmah.items.serializers import ItemSerializer
from bayt_al_hikmah.mixins.views import ActionPermDictMixin
from bayt_al_hikmah.permissions import DenyAll, IsInstructor, IsItemOwner
from bayt_al_hikmah.ui.mixins import UserAIMixin


# Create your views here.
class BaseItemVS(ActionPermDictMixin, UserAIMixin, ModelViewSet):
    """Base ViewSet for extension"""

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated, IsInstructor]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["lesson__module__course", "lesson__module", "lesson", "type"]
    action_perm_dict = {
        "default": permission_classes,
        "create": permission_classes + [IsItemOwner],
    }

    @action(methods=["post"], detail=True)
    def mark(self, request: Request, pk: int) -> Response:
        """Mark a course lesson item as un/completed"""

        is_completed = False
        item = self.get_object()

        if not request.user.items.contains(item):
            is_completed = True
            request.user.items.add(item)

        else:
            request.user.items.remove(item)

        item.save()

        return Response(
            {
                "details": f"Item '{item}' marked as {'completed' if is_completed else 'uncompleted'}"
            },
            status=status.HTTP_200_OK,
        )


class ItemViewSet(BaseItemVS):
    """View, update and delete Items"""

    action_perm_dict = {**BaseItemVS.action_perm_dict, "create": [DenyAll]}


class LessonItemsVS(BaseItemVS):
    """Create, view, update and delete Lesson Items"""

    def perform_create(self, serializer):
        """Add lesson to item automatically"""

        serializer.save(lesson_id=self.kwargs["lesson_id"])

    def get_queryset(self):
        """Filter queryset by lesson"""

        return super().get_queryset().filter(lesson_id=self.kwargs["lesson_id"])
