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
    path('oauth/', app.views.oauth, name="oauth"),

    path('board/boothPromotion', app.views.boothPromotion, name="boothPromotion"),
    path('board/friends', app.views.friends, name="friends"),

    path('board/boothPromotionNew', app.views.boothPromotionNew, name="boothPromotionNew"),
    path('board/friendsNew', app.views.friendsNew, name="friendsNew"),

    path('board/boothPromotionCreate', app.views.boothPromotionCreate, name="boothPromotionCreate"),
    path('board/friendsCreate', app.views.friendsCreate, name="friendsCreate"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
