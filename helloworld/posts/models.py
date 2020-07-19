from django.db import models


class Post(models.Model):
    title = models.CharField("Title", max_length=200)
    text = models.TextField("Text", blank=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
