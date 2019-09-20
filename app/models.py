from django.db import models
from django.utils import timezone


# Create your models here.
class Comment(models.Model):
    user = models.CharField(max_length=20)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)


# 분실물 게시판
class Board(models.Model):
    title = models.CharField(max_length=20)
    user = models.CharField(max_length=20)
    user_id = models.BigIntegerField(null=True)
    body = models.TextField()

    tag_choices = (
        ('found', '주웠어요'),
        ('lost', '잃어버렸어요')
    )

    tag = models.CharField(max_length=6, choices=tag_choices, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='board/images/%Y/%m/%d/%H/%M', blank=True, null=True)
    photo_delete_choices = (
        ('no', '기존 사진을 지우지 않습니다.'),
        ('yes', '기존 사진을 지웁니다.')
    )
    photo_delete = models.CharField(max_length=20, choices=photo_delete_choices, default=1, null=True)
    profile = models.CharField(max_length=150)

    def __str__(self):
        return self.title

# ################# 삭제 #################
# # 부스 홍보 게시판
# class BoothPromotionBoard(models.Model):
#     title = models.CharField(max_length=20)
#     user = models.CharField(max_length=20)
#     body = models.TextField()
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     photo = models.ImageField(upload_to='boothPromotionBoard/images/%Y/%m/%d/%H/%M', blank=True, null=True)
#     profile = models.CharField(max_length=150)
#
#     def __str__(self):
#         return self.title
# ################# 삭제 #################

# 술 친구 게시판
class FriendsBoard(models.Model):
    title = models.CharField(max_length=20)
    user = models.CharField(max_length=20)
    user_id = models.BigIntegerField(null=True)
    body = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='friends/images/%Y/%m/%d/%H/%M', blank=True, null=True)
    profile = models.CharField(max_length=150)

    def __str__(self):
        return self.title


# ################# 삭제 #################
# # 자유 게시판
# class FreeBoard(models.Model):
#     title = models.CharField(max_length=20)
#     user = models.CharField(max_length=20)
#     body = models.TextField()
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     photo = models.ImageField(upload_to='free/images/%Y/%m/%d/%H/%M', blank=True, null=True)
#     profile = models.CharField(max_length=150)
#     video = models.FileField(upload_to='free/videos/%Y/%m/%d/%H/%M', blank=True, null=True)
#
#     def __str__(self):
#         return self.title
# ################# 삭제 #################
