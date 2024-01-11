""" API endpoints for learn """


from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from learn.serializers import UserSerializer


# Create your views here.
User = get_user_model()


class UserViewSet(ModelViewSet):
    """Create, view, update and delete User profiles"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    search_fields = []
    ordering_fields = []
    filterset_fields = []
