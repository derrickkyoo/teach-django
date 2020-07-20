from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField("Age", null=True, blank=True)
    bio = models.TextField("Bio", blank=True)
