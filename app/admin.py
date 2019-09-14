from django.contrib import admin
from .models import Board, Comment

# Register your models here.
myModels = [Board, Comment]
admin.site.register(myModels)

