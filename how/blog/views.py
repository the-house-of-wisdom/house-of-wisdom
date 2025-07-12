"""API endpoints for how.blog"""

from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from how.api.mixins import ActionPermissionsMixin
from how.blog.models import Article
from how.blog.serializers import ArticleSerializer


# Create your views here.
class ArticleViewSet(ActionPermissionsMixin, ModelViewSet):
    """
    API endpoints for managing Articles.

    ## Overview

    API endpoints provides full CRUD (Create, Retrieve, Update, Delete) functionality for articles.
    These articles are designed to allow administrators to publish announcements, updates, or important notices.

    Only authorized admins can create, update, or delete articles, while enrolled students have read-only access.

    ## Endpoints

    - **List Articles**
        `GET /api/articles`
        Retrieves a list of all articles. Supports filtering by course and/or keywords in the article title or content.

    - **Create Article**
        `POST /api/articles`
        Creates a new article. Requires admin credentials and article details in the request body.

    - **Retrieve Article**
        `GET /api/articles/{id}`
        Retrieves detailed information for a specific article identified by `id`.

    - **Update Article**
        `PUT /api/articles/{id}`
        Fully updates an existing article with new details provided in the request body.

    - **Partial Update Article**
        `PATCH /api/articles/{id}`
        Applies partial updates to an existing article (e.g., updating the article content).

    - **Delete Article**
        `DELETE /api/articles/{id}`
        Deletes the article identified by `id`.

    ## Query Parameters

    - **search:**
        Filter articles by title or content keywords (e.g., `?search=update`).

    - **ordering:**
        Order articles by a specific field (e.g., `?ordering=-created_at` to list the most recent articles first).

    ## Permissions

    - **Instructors/Students:**
        Can view articles related to the courses in which they are enrolled.

    - **Admins:**
        Can create, update, and delete articles for courses they manage.

    ## Example API Requests

    **List Articles:**

    ```bash
    curl -X GET /api/articles
    ```

    **Create an Article:**

    ```bash
    curl -X POST /api/articles \\
        -H "Content-Type: application/json" \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE" \\
        -d '{
                "title": "Announcing the new updates!",
                "content": "We are excited to share..."
            }'
    ```

    **Partial Update (e.g., Update Content):**

    ```bash
    curl -X PATCH /api/articles/5 \\
        -H "Content-Type: application/json" \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE" \\
        -d '{
                "content": "Please note that the..."
            }'
    ```

    **Delete an Article:**

    ```bash
    curl -X DELETE /api/articles/5 \\
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
    ```

    ## Additional Notes

    Articles serve as a central communication tool within the platform, ensuring that users are constantly
    updated with the latest news. By using the this API, admins can create an engaging, informative, and dynamic environment.
    """

    queryset = Article.objects.live()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["title", "headline", "content"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["owner"]
    action_permissions = {
        "default": [IsAuthenticated, IsAdminUser],
        "list": permission_classes,
        "retrieve": permission_classes,
    }

    def get_queryset(self):
        """Filter queryset by owner"""

        return super().get_queryset().filter(owner_id=self.request.user.id)
