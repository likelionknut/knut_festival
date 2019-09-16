from django import forms
from .models import Comment
from .models import Board


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'text',)


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board

        fields = ['title', 'user', 'body', 'photo']

        exclude = ['user']

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
                attrs={'class': 'form-control'}
            ),

        }
