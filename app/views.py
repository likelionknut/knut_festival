from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Comment, Board
from .forms import CommentForm
from django.core.paginator import Paginator
import requests

# Create your views here.

def home(request):
    comments = Comment.objects.all()
    boards_list = Board.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'comments':comments, 'boards_list':boards_list})


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

    boards_list = Board.objects.all().order_by('-created_at')
    paginator = Paginator(boards_list, 5) # 게시물 5개를 기준으로 페이지네이션 전개
    page = request.GET.get('page')        # request 된 페이지를 변수에 담음
    posts = paginator.get_page(page)

    return render(request, 'board.html', {'posts':posts})

def new(request):
    return render(request, 'new.html')

# 제출 버튼을 누른뒤 작성한 게시글 detail로 보내기 위한 함수
def create(request):

    title = request.GET['title']
    body = request.GET['body']
    created_at = timezone.datetime.now()

    request.session['title'] = str(title)
    request.session['body'] = str(body)
    request.session['created_at'] = str(created_at)


    login_request_uri = 'https://kauth.kakao.com/oauth/authorize?'

    client_id = 'd9079dbac88fca9754d091a7af0366ed'
    redirect_uri = 'http://127.0.0.1:8000/oauth'

    login_request_uri += 'client_id=' + client_id
    login_request_uri += '&redirect_uri=' + redirect_uri
    login_request_uri += '&response_type=code'

    request.session['client_id'] = client_id
    request.session['redirect_uri'] = redirect_uri

    return redirect(login_request_uri)
    # return redirect('board')


# 카카오톡 oauth
def oauth(request):
    code = request.GET['code']
    print('code = ' + str(code))

    client_id = request.session.get('client_id')
    redirect_uri = request.session.get('redirect_uri')

    access_token_request_uri = "https://kauth.kakao.com/oauth/token?grant_type=authorization_code&"

    access_token_request_uri += "client_id=" + client_id
    access_token_request_uri += "&redirect_uri=" + redirect_uri
    access_token_request_uri += "&code=" + code

    print(access_token_request_uri)

    access_token_request_uri_data = requests.get(access_token_request_uri)
    json_data = access_token_request_uri_data.json()
    access_token = json_data['access_token']
    print(access_token)

    user_profile_info_uri = "https://kapi.kakao.com/v1/api/talk/profile?access_token="
    user_profile_info_uri += str(access_token)

    user_profile_info_uri_data = requests.get(user_profile_info_uri)
    user_json_data = user_profile_info_uri_data.json()
    nickName = user_json_data['nickName']
    profileImageURL = user_json_data['profileImageURL']
    thumbnailURL = user_json_data['thumbnailURL']

    print("nickName = " + str(nickName))
    print("profileImageURL = " + str(profileImageURL))
    print("thumbnailURL = " + str(thumbnailURL))

    board = Board()
    board.title = request.session.get('title')
    board.body = request.session.get('body')
    board.user = nickName
    board.created_at = request.session.get('created_at')
    board.save()

    return redirect('board')