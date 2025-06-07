"""Tests for how.questions.views"""

from rest_framework.test import APITestCase


# Create your tests here.
class QuestionViewSetTests(APITestCase):
    """Question ViewSet tests"""

    def setUp(self) -> None:
        """Setup before running tests"""
