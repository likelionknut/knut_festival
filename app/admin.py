from django.contrib import admin
# from .models import Board, Comment, BoothPromotionBoard, FriendsBoard, FreeBoard
from .models import Board, Comment, FriendsBoard

# Register your models here.
# myModels = [Board, Comment, BoothPromotionBoard, FriendsBoard, FreeBoard]
myModels = [Board, Comment, FriendsBoard]
admin.site.register(myModels)

