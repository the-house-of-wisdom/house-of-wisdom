"""API endpoints for how.apps.categories"""

from rest_framework.permissions import IsAdminUser, IsAuthenticated
from wagtail.api.v2.views import PagesAPIViewSet

from how.api.mixins import ActionPermissionsMixin
from how.apps.categories.models import Category


# Create your views here.
class CategoryViewSet(ActionPermissionsMixin, PagesAPIViewSet):
    """
    API endpoints for managing Categories.

    ## Overview

    API endpoints provide full CRUD (Create, Retrieve, Update, Delete) functionality for course categories.
    Categories help organize courses into thematic or subject-related groupings, making it easier for users
    to explore and filter available courses.

    ## Endpoints

    - **List Categories**
      `GET /api/categories`
      Retrieves a list of all course categories.

    - **Create Category**
      `POST /api/categories`
      Creates a new course category. Requires category details in the request body.

    - **Retrieve Category**
      `GET /api/categories/{id}`
      Retrieves detailed information for the category identified by `id`.

    - **Update Category**
      `PUT /api/categories/{id}`
      Fully updates an existing course category with the provided information.

    - **Partial Update Category**
      `PATCH /api/categories/{id}`
      Applies partial updates to the category.

    - **Delete Category**
      `DELETE /api/categories/{id}`
      Deletes the course category identified by `id`.

    ## Query Parameters

    - **search:**
      Filter categories by title or description (e.g., `?search=technology`).

    - **ordering:**
      Order categories by a specific field (e.g., `?ordering=title` for alphabetical order).

    ## Permissions

    - **Authenticated Users:**
      Can view the list of categories and retrieve category details.

    - **Admin/Staff Users:**
      Can create, update, or delete categories.

    ## Example API Requests

    **List Categories:**

    ```bash
    curl -X GET /api/categories \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    **Create a Category:**

    ```bash
    curl -X POST /api/categories \\
        -H "Content-Type: application/json" \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE" \\
        -d '{
                "title": "Technology",
                "description": "Courses related to technology, programming, and IT."
            }'
    ```

    **Retrieve Category Details:**

    ```bash
    curl -X GET /api/categories/1 \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```
    """

    model = Category
    name = "categories"
    permission_classes = [IsAuthenticated]
    ordering_fields = ["created_at", "updated_at"]
    action_permissions = {
        "default": [IsAuthenticated, IsAdminUser],
        "list": permission_classes,
        "retrieve": permission_classes,
    }
