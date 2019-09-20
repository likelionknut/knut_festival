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

        help_texts = {
            'title': '글 제목',
            'tag': '주웠어요/잃어버렸어요',
            'body': '본문 내용',
            'photo': '사진 업로드',
        }

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'text-transform: none;', 'placeholder': '제목을 입력하세요.'}
            ),
            'tag': forms.Select(
                attrs={'class': 'custom-select', 'placeholder': '제목을 입력하세요.'}
            ),
            'body': forms.Textarea(
                attrs={'class': 'form-control', 'style': 'text-transform: none;', 'rows': 20}
            ),
            'photo': forms.FileInput(
                attrs={'class': 'form-control-file',
                       'accept': 'image/*',
                       'style': 'border: 1px solid #ccc; display: inline-block; cursor: pointer;'}
            ),
        }


# ################# 삭제 #################
# # 부스 홍보 게시판
# class BoothPromotionForm(forms.ModelForm):
#     class Meta:
#         model = BoothPromotionBoard
#
#         fields = ['title', 'profile', 'user', 'body', 'photo', ]
#
#         exclude = ['user', 'profile']
#
#         help_texts = {
#             'title': '글 제목',
#             'body': '본문 내용',
#             'photo': '사진 업로드',
#         }
#
#         widgets = {
#             'title': forms.TextInput(
#                 attrs={'class': 'form-control', 'style': 'text-transform: none;', 'placeholder': '제목을 입력하세요.'}
#             ),
#             'body': forms.Textarea(
#                 attrs={'class': 'form-control', 'style': 'text-transform: none;', 'cols': 80, 'rows': 20}
#             ),
#             'photo': forms.FileInput(
#                 attrs={'class': 'form-control-file',
#                        'accept': 'image/*',
#                        'style': 'border: 1px solid #ccc; display: inline-block; cursor: pointer;'}
#             ),
#         }
# ################# 삭제 #################


# 술 친구 게시판
class FriendsForm(forms.ModelForm):
    class Meta:
        model = FriendsBoard

        fields = ['title', 'profile', 'user', 'body', 'photo', ]

        exclude = ['user', 'profile']

        help_texts = {
            'title': '글 제목',
            'body': '본문 내용',
            'photo': '사진 업로드',
        }

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'text-transform: none;', 'placeholder': '제목을 입력하세요.'}
            ),
            'body': forms.Textarea(
                attrs={'class': 'form-control', 'style': 'text-transform: none;', 'cols': 80, 'rows': 20}
            ),
            'photo': forms.FileInput(
                attrs={'class': 'form-control-file',
                       'accept': 'image/*',
                       'style': 'border: 1px solid #ccc; display: inline-block; cursor: pointer;'}
            ),
        }


# ################# 삭제 #################
# # 자유 게시판
# class FreeForm(forms.ModelForm):
#
#     class Meta:
#         model = FreeBoard
#
#         fields = ['title', 'profile', 'user', 'body', 'photo', 'video']
#
#         exclude = ['user', 'profile']
#
#         help_texts = {
#             'title': '글 제목',
#             'body': '본문 내용',
#             'photo': '사진 업로드',
#             'video': '동영상 업로드',
#         }
#
#         widgets = {
#             'title': forms.TextInput(
#                 attrs={'class': 'form-control', 'style': 'text-transform: none;', 'placeholder': '제목을 입력하세요.'}
#             ),
#             'body': forms.Textarea(
#                 attrs={'class': 'form-control', 'style': 'text-transform: none;', 'cols': 80, 'rows': 20}
#             ),
#             'photo': forms.FileInput(
#                 attrs={'class': 'form-control-file',
#                        'accept': 'image/*',
#                        'style': 'border: 1px solid #ccc; display: inline-block; cursor: pointer;'}
#             ),
#             'video': forms.FileInput(
#                 attrs={'class': 'form-control-file',
#                        'accept': 'file_extension|audio/*|video/*|image/*|media_type',
#                        # 'style': 'background-color: #ccc; border: 1px solid gray; padding: 6px 12px;'}
#                        'style': 'border: 1px solid #ccc; display: inline-block; cursor: pointer;'}
#             )
#
#         }
# ################# 삭제 #################
