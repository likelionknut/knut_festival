from django.db import models
from django.utils import timezone


# Create your models here.
class Comment(models.Model):
    user = models.CharField(max_length=20)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)



class Board(models.Model):
    title = models.CharField(max_length=20)
    user = models.CharField(max_length=10)
    body = models.TextField()

    tag_choices = (
        ('found', '주웠어요'),
        ('lost', '잃어버렸어요')
    )

    tag = models.CharField(max_length=6, choices=tag_choices, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title
