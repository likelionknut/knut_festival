from django.db import models
from django.utils import timezone

# Create your models here.

class Lost(models.Model):
    user = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images/')
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title