from django.contrib import admin
from .models import Board, Comment, FriendsBoard


# Register your models here.
# myModels = [Board, Comment, BoothPromotionBoard, FriendsBoard, FreeBoard]
# myModels = [Board, Comment, FriendsBoard]
# admin.site.register(myModels)

class BoardAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

    fieldsets = [
        ('글 제목', {'fields': ['title']}),
        ('주웠어요/잃어버렸어요', {'fields': ['tag']}),
        ('글 내용', {'fields': ['body']}),
        ('사용자', {'fields': ['user', 'user_id', 'profile_url', 'profile']}),
        ('사진', {'fields': ['photo']}),
    ]

    list_display = ['id', 'title', 'tag', 'user', 'user_id', 'created_at']
    list_display_links = ['id', 'title']
    list_per_page = 10

    list_filter = ['tag', 'created_at']


class FriendsBoardAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

    fieldsets = [
        ('글 제목', {'fields': ['title']}),
        ('글 내용', {'fields': ['body']}),
        ('사용자', {'fields': ['user', 'user_id', 'profile_url', 'profile']}),
        ('사진', {'fields': ['photo']}),
    ]

    list_display = ['id', 'title', 'user', 'user_id', 'created_at']
    list_display_links = ['id', 'title']
    list_per_page = 10

    list_filter = ['created_at']


admin.site.register(Board, BoardAdmin)
admin.site.register(FriendsBoard, FriendsBoardAdmin)
