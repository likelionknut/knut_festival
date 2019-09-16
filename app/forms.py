from django import forms
from .models import Comment
from .models import Board

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user','text',)


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board

        fields = ['title', 'body', 'photo']
