from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Comment, Board
from .forms import CommentForm
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    comments = Comment.objects.all()
    return render(request, 'index.html', {'comments':comments})


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


# def login(request):
#     return render(request, 'index.html')



# primary key 값을 부여해서 게시글 마다 고유한 번호를 가질수 있게 설계 (게시글 구분)
def detail(request, board_id):
    board_detail = get_object_or_404(Board, pk=board_id)
    return render(request, 'detail.html', {'board' : board_detail})

def board(request):

    boards = Board.objects
    boards_list = Board.objects.all().order_by('-created_at')
    paginator = Paginator(boards_list, 5) # 게시물 5개를 기준으로 페이지네이션 전개
    page = request.GET.get('page')        # request 된 페이지를 변수에 담음
    posts = paginator.get_page(page)

    return render(request, 'board.html', {'boards':boards, 'posts':posts})

def new(request):
    return render(request, 'new.html')

# 제출 버튼을 누른뒤 작성한 게시글 detail로 보내기 위한 함수
def create(request):
    board = Board()
    board.title = request.GET['title']
    board.body = request.GET['body']
    board.user = request.GET['user']
    board.created_at = timezone.datetime.now()
    board.save()
    return redirect('/board/')


# 카카오톡 oauth
def oauth(request):
    return redirect('board')