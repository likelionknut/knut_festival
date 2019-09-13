from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Comment
from .forms import CommentForm
from find.models import Lost

# Create your views here.

def home(request):
    comments = Comment.objects.all()
    losts = Lost.objects.all()
    return render(request, 'index.html', {'comments':comments, 'losts':losts})

def comment_write(request):
    if request.method == 'POST':
        comments = Comment.objects.all()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            user = request.user.username
            comment.user = user
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()
        comments = Comment.objects.all()
    return render(request, 'index.html', {'form':form, 'comments':comments})

def login(request):
    return render(request, 'index.html')