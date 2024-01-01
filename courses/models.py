""" Data Models for learn.courses """


from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Course(AbstractUser):
    """Courses"""

    pass
