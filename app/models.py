from django.db import models
from django.utils import timezone
from urllib.request import urlopen
from django.core.files import File
import os
from tempfile import NamedTemporaryFile


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
    profile_url = models.URLField(null=True)
    profile = models.ImageField(upload_to='board/profile/%Y/%m/%d/%H/%M', null=True)
    page_counter = models.BigIntegerField(default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.profile_url and not self.profile:
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(self.profile_url).read())
            img_temp.flush()
            # self.profile.save(f"image_{self.pk}", File(img_temp))
            self.profile.save(os.path.basename(self.profile_url), File(img_temp))
        super(Board, self).save(*args, **kwargs)

    # def get_remote_image(self):
    #     if self.profile_url and not self.profile:
    #         result = urllib.urlretrieve(self.profile_url)
    #         self.profile.save(
    #             os.path.basename(self.profile_url),
    #             File(open(result[0]))
    #         )
    #         # self.save()

    # def get_remote_image(self):
    #     if self.profile_url:
    #         # result = urllib.request.urlretrieve(self.profile_url, 'download.jpg')
    #         urllib.request.urlretrieve(self.profile_url, 'E:\download.jpg')
    #         # self.profile.save(
    #         #     os.path.basename(self.profile_url),
    #         #     File(open(result[0]))
    #         # )
    #         # self.save()


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
    # profile = models.CharField(max_length=150)
    profile_url = models.URLField(null=True)
    profile = models.ImageField(upload_to='friends/profile/%Y/%m/%d/%H/%M', null=True)
    page_counter = models.BigIntegerField(default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.profile_url and not self.profile:
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(self.profile_url).read())
            img_temp.flush()
            # self.profile.save(f"image_{self.pk}", File(img_temp))
            self.profile.save(os.path.basename(self.profile_url), File(img_temp))
        super(FriendsBoard, self).save(*args, **kwargs)

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
