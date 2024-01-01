""" Data Models for learn.specializations """


from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Specialization(AbstractUser):
    """Specializations, collections of related courses"""

    pass
