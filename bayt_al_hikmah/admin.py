"""Admin site for Bayt Al-Hikmah"""

from django.contrib import admin

from bayt_al_hikmah.answers.models import Answer
from bayt_al_hikmah.assignments.models import Assignment
from bayt_al_hikmah.categories.models import Category
from bayt_al_hikmah.collections.models import Collection
from bayt_al_hikmah.courses.models import Course
from bayt_al_hikmah.enrollments.models import Enrollment
from bayt_al_hikmah.items.models import Item
from bayt_al_hikmah.modules.models import Module
from bayt_al_hikmah.notifications.models import Notification
from bayt_al_hikmah.questions.models import Question
from bayt_al_hikmah.reviews.models import Review
from bayt_al_hikmah.lessons.models import Lesson
from bayt_al_hikmah.submissions.models import Submission
from bayt_al_hikmah.tags.models import Tag
from bayt_al_hikmah.users.models import User


# Create your model inlines here.
class ModuleInline(admin.StackedInline):
    """
    Module Inline
    """

    model = Module
    extra = 0


class ReviewInline(admin.StackedInline):
    """
    Review Inline
    """

    model = Review
    extra = 0


class LessonInline(admin.StackedInline):
    """
    Lesson Inline
    """

    model = Lesson
    extra = 0


class ItemInline(admin.StackedInline):
    """
    Item Inline
    """

    model = Item
    extra = 0


class AssignmentInline(admin.StackedInline):
    """
    Assignment Inline
    """

    model = Assignment
    extra = 0


class QuestionInline(admin.StackedInline):
    """
    Question Inline
    """

    model = Question
    extra = 0


class AnswerInline(admin.StackedInline):
    """
    Answer Inline
    """

    model = Answer
    extra = 0


class SubmissionInline(admin.StackedInline):
    """
    Submission Inline
    """

    model = Submission
    extra = 0


# Create your model admins here.
@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    """
    Collection ModelAdmin
    """

    model = Collection
    date_hierarchy = "created_at"
    search_fields = ["name", "headline", "description"]
    list_filter = ["created_at", "updated_at"]
    list_display = [
        "id",
        "name",
        "created_at",
        "updated_at",
    ]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """
    Course ModelAdmin
    """

    model = Course
    date_hierarchy = "created_at"
    inlines = [ModuleInline, ReviewInline]
    search_fields = ["name", "headline", "description"]
    list_filter = ["created_at", "updated_at"]
    list_display = ["id", "name", "created_at", "updated_at"]


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    """
    Module ModelAdmin
    """

    model = Module
    date_hierarchy = "created_at"
    inlines = [LessonInline]
    search_fields = ["title", "description"]
    list_filter = ["created_at", "updated_at"]
    list_display = ["id", "title", "created_at", "updated_at"]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """
    Lesson ModelAdmin
    """

    model = Lesson
    date_hierarchy = "created_at"
    inlines = [ItemInline, AssignmentInline]
    search_fields = ["name", "description"]
    list_filter = ["created_at", "updated_at"]
    list_display = ["id", "name", "created_at", "updated_at"]


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    """
    Assignment ModelAdmin
    """

    model = Assignment
    date_hierarchy = "created_at"
    inlines = [QuestionInline]
    search_fields = ["title", "description"]
    list_filter = ["created_at", "updated_at"]
    list_display = ["id", "lesson", "title", "created_at", "updated_at"]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """
    Question ModelAdmin
    """

    model = Question
    date_hierarchy = "created_at"
    inlines = [AnswerInline]
    search_fields = ["text"]
    list_filter = ["created_at", "updated_at"]
    list_display = ["id", "assignment", "type", "created_at", "updated_at"]


# Register your models here.
admin.site.register(Answer)
admin.site.register(Category)
admin.site.register(Enrollment)
admin.site.register(Item)
admin.site.register(Notification)
admin.site.register(Submission)
admin.site.register(Tag)
admin.site.register(User)
