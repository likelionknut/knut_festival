from django.contrib import admin
from .models import Board, Comment, BoothPromotionBoard, FriendsBoard, FreeBoard

# Register your models here.
myModels = [Board, Comment, BoothPromotionBoard, FriendsBoard, FreeBoard]
admin.site.register(myModels)

