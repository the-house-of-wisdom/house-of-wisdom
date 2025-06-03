"""Data Models for bayt_al_hikmah.tags"""

from django.db import models
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase


# Create your models here.
class ArticleTag(TaggedItemBase):
    content_object = ParentalKey(
        "blog.Article",
        related_name="tagged_items",
        on_delete=models.CASCADE,
    )


class LearningPathTag(TaggedItemBase):
    content_object = ParentalKey(
        "paths.LearningPath",
        related_name="tagged_items",
        on_delete=models.CASCADE,
    )


class CourseTag(TaggedItemBase):
    content_object = ParentalKey(
        "courses.Course",
        related_name="tagged_items",
        on_delete=models.CASCADE,
    )
