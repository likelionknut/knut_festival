"""knut_festival URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import app.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.views.home, name="home"),
    # path('1/', app.views.comment_write, name="comment_write"),
    # path('2/', app.views.login, name="login"),
    # path('accounts/', include('allauth.urls')),

    path('board/', app.views.board, name="board"),
    path('board/<int:board_id>/', app.views.detail, name="detail"),
    path('board/new/', app.views.new, name="new"),
    path('board/create/', app.views.create, name="create"),
    path('board/<int:board_id>/delete', app.views.delete, name="delete"),
    path('board/<int:board_id>/edit', app.views.edit, name="edit"),

    path('kakao/', app.views.kakao, name="kakao"),
    path('oauth/', app.views.oauth, name="oauth"),

    # ################# 삭제 #################
    # path('board/boothPromotion', app.views.boothPromotion, name="boothPromotion"),
    # path('board/boothPromotionNew', app.views.boothPromotionNew, name="boothPromotionNew"),
    # path('board/boothPromotionCreate', app.views.boothPromotionCreate, name="boothPromotionCreate"),
    # path('board/boothPromotion/<int:board_id>/', app.views.boothPromotionDetail, name="boothPromotionDetail"),
    # ################# 삭제 #################

    path('board/friends', app.views.friends, name="friends"),
    path('board/friendsNew', app.views.friendsNew, name="friendsNew"),
    path('board/friendsCreate', app.views.friendsCreate, name="friendsCreate"),
    path('board/friends/<int:board_id>/', app.views.friendsDetail, name="friendsDetail"),
    # path('board/friends/<int:board_id>/delete', app.views.friendsDelete, name="friendsDelete"),

    # ################# 삭제 #################
    # path('board/free', app.views.free, name="free"),
    # path('board/freeNew', app.views.freeNew, name="freeNew"),
    # path('board/freeCreate', app.views.freeCreate, name="freeCreate"),
    # path('board/free/<int:board_id>/', app.views.freeDetail, name="freeDetail"),
    # ################# 삭제 #################

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
