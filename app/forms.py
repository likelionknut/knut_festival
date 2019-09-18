from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'text',)


# 분실물 게시판
class BoardForm(forms.ModelForm):
    class Meta:
        model = Board

        fields = ['title', 'tag', 'profile', 'user', 'body', 'photo', ]

        exclude = ['user', 'profile']

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
            ),
            'tag': forms.Select(
                attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
            ),
            # 'user': forms.TextInput(
            #     attrs={'readonly': 'readonly'}
            # ),
            'body': forms.Textarea(
                attrs={'class': 'form-control', 'cols': 80, 'rows': 20}
            ),
            # 'author': forms.Select(
            #     attrs={'class': 'custom-select'},
            # ),
            'photo': forms.FileInput(
                attrs={'class': 'form-control',
                       'accept': 'image/*',
                       'style': 'border: 1px solid #ccc; display: inline-block; cursor: pointer;'}
            ),

        }


# 부스 홍보 게시판
class BoothPromotionForm(forms.ModelForm):
    class Meta:
        model = BoothPromotionBoard

        fields = ['title', 'profile', 'user', 'body', 'photo', ]

        exclude = ['user', 'profile']

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
            ),
            # 'user': forms.TextInput(
            #     attrs={'readonly': 'readonly'}
            # ),
            'body': forms.Textarea(
                attrs={'class': 'form-control', 'cols': 80, 'rows': 20}
            ),
            # 'author': forms.Select(
            #     attrs={'class': 'custom-select'},
            # ),
            'photo': forms.FileInput(
                attrs={'class': 'form-control',
                       'accept': 'image/*',
                       'style': 'border: 1px solid #ccc; display: inline-block; cursor: pointer;'}
            ),

        }


# 술 친구 게시판
class FriendsForm(forms.ModelForm):
    class Meta:
        model = FriendsBoard

        fields = ['title', 'profile', 'user', 'body', 'photo', ]

        exclude = ['user', 'profile']

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
            ),
            # 'user': forms.TextInput(
            #     attrs={'readonly': 'readonly'}
            # ),
            'body': forms.Textarea(
                attrs={'class': 'form-control', 'cols': 80, 'rows': 20}
            ),
            # 'author': forms.Select(
            #     attrs={'class': 'custom-select'},
            # ),
            'photo': forms.FileInput(
                attrs={'class': 'form-control',
                       'accept': 'image/*',
                       'style': 'border: 1px solid #ccc; display: inline-block; cursor: pointer;'}
            ),

        }


# 자유 게시판
class FreeForm(forms.ModelForm):
    class Meta:
        model = FreeBoard

        fields = ['title', 'profile', 'user', 'body', 'photo', 'video']

        exclude = ['user', 'profile']

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
            ),
            # 'user': forms.TextInput(
            #     attrs={'readonly': 'readonly'}
            # ),
            'body': forms.Textarea(
                attrs={'class': 'form-control', 'cols': 80, 'rows': 20}
            ),
            # 'author': forms.Select(
            #     attrs={'class': 'custom-select'},
            # ),
            'photo': forms.FileInput(
                attrs={'class': 'form-control-file',
                       'accept': 'image/*',
                       'style': 'border: 1px solid #ccc; display: inline-block; cursor: pointer;'}
            ),
            'video': forms.FileInput(
                attrs={'class': 'form-control-file',
                       'accept': 'file_extension|audio/*|video/*|image/*|media_type',
                       # 'style': 'background-color: #ccc; border: 1px solid gray; padding: 6px 12px;'}
                       'style': 'border: 1px solid #ccc; display: inline-block; cursor: pointer;'}
            )

        }
