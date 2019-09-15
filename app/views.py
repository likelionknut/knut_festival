from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Comment, Board
from .forms import CommentForm
from find.models import Lost

# Create your views here.

def home(request):
    comments = Comment.objects.all()

    losts = Lost.objects.all()
    # return render(request, 'index.html', {'comments':comments, 'losts':losts})

    boards = Board.objects.all()

    return render(request, 'index.html', {'comments':comments, 'boards':boards, 'losts':losts})


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

    # return render(request, 'index.html', {'form':form, 'comments':comments})

def detail(request, board_id):
    board_detail = get_object_or_404(Board, pk=board_id)
    return render(request, 'detail.html', {'board' : board_detail})

def board(request):
    boards = Board.objects.all()
    return render(request, 'board.html', {'boards':boards})
