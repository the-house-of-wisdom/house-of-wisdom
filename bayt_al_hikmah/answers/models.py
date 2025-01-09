""" Data Models for bayt_al_hikmah.answers """

from django.db import models


# Create your models here.
class Answer(models.Model):
    """Question Answers"""

    question = models.ForeignKey(
        "questions.Question",
        on_delete=models.CASCADE,
        related_name="answers",
        help_text="Answer question",
    )
    is_correct = models.BooleanField(
        default=False,
        help_text="Weather the answer is correct",
    )
    text = models.CharField(
        max_length=64,
        help_text="Answer text",
    )
    description = models.CharField(
        max_length=512,
        help_text="Why the answer is correct or wrong",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )

    def __str__(self) -> str:
        return f"{self.question}: Answer {self.pk}"
