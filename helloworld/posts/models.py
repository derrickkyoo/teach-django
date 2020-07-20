from django.conf import settings
from django.db import models


class Post(models.Model):
    title = models.CharField("Title", max_length=200)
    text = models.TextField("Text", blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.title
