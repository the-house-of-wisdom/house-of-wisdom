"""Tests for how.apps.posts.views"""

from rest_framework.test import APITestCase


# Create your tests here.
class PostViewSetTests(APITestCase):
    """Post ViewSet test"""

    def setUp(self) -> None:
        """Setup before running tests"""
