"""Data Models for how.tags"""

from django.db import models
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase


# Create your models here.
class ArticleTag(TaggedItemBase):
    """Through model for defining m2m rel between Articles and Tags"""

    content_object = ParentalKey(
        "blog.Article",
        related_name="tagged_items",
        on_delete=models.CASCADE,
    )


class LearningPathTag(TaggedItemBase):
    """Through model for defining m2m rel between LearningPaths and Tags"""

    content_object = ParentalKey(
        "paths.LearningPath",
        related_name="tagged_items",
        on_delete=models.CASCADE,
    )


class CourseTag(TaggedItemBase):
    """Through model for defining m2m rel between Courses and Tags"""

    content_object = ParentalKey(
        "courses.Course",
        related_name="tagged_items",
        on_delete=models.CASCADE,
    )
