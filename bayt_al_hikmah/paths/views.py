"""API endpoints for bayt_al_hikmah.paths"""

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.mixins.views import ActionPermissionsMixin, OwnerMixin
from bayt_al_hikmah.paths.models import Path
from bayt_al_hikmah.paths.serializers import PathSerializer
from bayt_al_hikmah.permissions import IsInstructor, IsOwner


# Create your views here.
class PathViewSet(ActionPermissionsMixin, OwnerMixin, ModelViewSet):
    """
    API endpoints for managing Learning Paths.

    ## Overview

    API endpoints provide full CRUD (Create, Retrieve, Update, Delete) functionality for learning paths.
    A learning path is a curated sequence of courses designed to guide learners through a specific subject
    area or to help them achieve defined career goals. Learning paths can include prerequisites, recommended courses,
    and sequencing information to ensure a cohesive learning experience.

    ## Endpoints

    - **List Learning Paths**
      `GET /api/paths`
      Retrieves a list of all learning paths.

    - **Create Learning Path**
      `POST /api/paths`
      Creates a new learning path. Requires learning path details in the request body.

    - **Retrieve Learning Path**
      `GET /api/paths/{id}`
      Retrieves detailed information for the learning path identified by `id`.

    - **Update Learning Path**
      `PUT /api/paths/{id}`
      Fully updates an existing learning path with the provided information.

    - **Partial Update Learning Path**
      `PATCH /api/paths/{id}`
      Applies partial updates to the learning path.

    - **Delete Learning Path**
      `DELETE /api/paths/{id}`
      Deletes the learning path identified by `id`.

    ## Query Parameters

    - **user:**
      Filter learning paths by instructor (e.g., `?user=1`).

    - **category:**
      Filter learning paths by category (e.g., `?category=1`).

    - **tags:**
      Filter learning paths by tags (e.g., `?tags=1`).

    - **search:**
      Filter learning paths by name, headline or description (e.g., `?search=python`).

    - **ordering:**
      Order learning paths by a specific field (e.g., `?ordering=name` for alphabetical order).

    ## Permissions

    - **Authenticated Users:**
      Can view, retrieve and save learning path details.

    - **Instructors/Admins:**
      Can create, update, and delete learning paths.

    ## Extra Actions

    In addition to the default CRUD operations, this viewset defines several custom actions to extend its functionality:

    - **Save a learning path:**
    Allows an authenticated user to save a learning path (add to favorites, save for later use, ...).
    `POST /api/paths/{id}/save`
    *Request:* No body is required.
    *Response:* Returns a confirmation message.

    ## Example API Requests

    **List Learning Paths:**

    ```bash
    curl -X GET http://localhost:8000/api/paths \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    **Create a Learning Path:**

    ```bash
    curl -X POST http://localhost:8000/api/paths \\
        -H "Content-Type: application/json" \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE" \\
        -d '{
                "category": 1,
                "image": "path/to/image.png",
                "name": "Data Science Essentials",
                "headline": "DS for beginners",
                "description": "A curated path to start your journey in data science.",
                "prerequisites": "Basic programming knowledge",
                "duration": "6 months",
                "courses": [1, 3, 5],  // Array of course IDs included in the path
                "tags": [1, 10, 25, 43, 12]  // Array of tag IDs associated with the path
            }'
    ```

    **Save a Learning Path:**

    ```bash
    curl -X POST http://localhost:8000/api/paths/2/save
    ```
    """

    queryset = Path.objects.all()
    serializer_class = PathSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "headline", "description"]
    ordering_fields = ["name", "created_at", "updated_at"]
    filterset_fields = ["user", "category", "tags"]
    action_permissions = {
        "default": [IsAuthenticated, IsInstructor, IsOwner],
        "list": permission_classes,
        "retrieve": permission_classes,
        "save": permission_classes,
    }

    @action(methods=["post"], detail=True)
    def save(self, request: Request, pk: int) -> Response:
        """Add a path to favorite or saved paths"""

        saved: bool = False
        path: Path = self.get_object()

        if request.user.saved.contains(path):
            request.user.saved.remove(path)

        else:
            saved = True
            request.user.saved.add(path)

        return Response(
            {
                "details": f"Path '{path}' {'added to' if saved else 'removed from'} your saved paths"
            },
            status=status.HTTP_200_OK,
        )
