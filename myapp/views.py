from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Comment
from .forms import CommentForm

# Create your views here.

def home(request):
    comments = Comment.objects.all()
    return render(request, 'index.html', {'comments':comments})

def comment_write(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()
        comments = Comment.objects.all()
    return render(request, 'index.html', {'form':form, 'comments':comments})