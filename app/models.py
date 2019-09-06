from django.db import models
from django.utils import timezone

# Create your models here.

class Comment(models.Model):
    user = models.CharField(max_length=10)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)