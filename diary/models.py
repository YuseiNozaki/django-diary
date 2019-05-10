from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=256)
    datetime = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
