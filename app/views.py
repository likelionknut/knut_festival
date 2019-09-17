from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Comment, Board, PromotionBoard, FriendsBoard
from .forms import CommentForm, BoardForm
from django.core.paginator import Paginator
import requests, math

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
    paginator = Paginator(boards_list, 6) # 게시물 5개를 기준으로 페이지네이션 전개
    page = request.GET.get('page', 1)        # request 된 페이지를 변수에 담음
    posts = paginator.get_page(page)
    page_range = 5                          # 5개의 페이지 블럭 (범위)
    current_block = math.ceil(int(page)/page_range)
    start_block = (current_block-1) * page_range
    end_block = start_block + page_range
    p_range = paginator.page_range[start_block:end_block]

    return render(request, 'boards/board.html', {'posts':posts, 'p_range':p_range})

# 글쓰기 버튼
def new(request):

    login_request_uri = 'https://kauth.kakao.com/oauth/authorize?'

    client_id = 'd9079dbac88fca9754d091a7af0366ed'
    redirect_uri = 'http://127.0.0.1:8000/oauth'

    login_request_uri += 'client_id=' + client_id
    login_request_uri += '&redirect_uri=' + redirect_uri
    login_request_uri += '&response_type=code'

    request.session['client_id'] = client_id
    request.session['redirect_uri'] = redirect_uri

    return redirect(login_request_uri)
    # return render(request, 'new.html')

# 제출 버튼을 누른뒤 작성한 게시글 detail로 보내기 위한 함수
def create(request):

    # board = Board()
    # board.title = request.GET['title']
    # board.body = request.GET['body']
    # board.created_at = timezone.datetime.now()
    # board.user = request.session.get('user')
    # print("title = "+board.title)
    # print("body = "+board.body)
    # print("user = "+board.user)
    # board.photo = request.FILES.get('photo')
    # board.save()

    if request.method == 'POST':
        form = BoardForm(request.POST, request.FILES)

        if form.is_valid():

            post = form.save(commit=False)

            post.user = request.session.get('user')
            post.profile = request.session.get('profile')
            post.save()

            return redirect('board')
        else:
            return redirect('board')
    else:
        form = BoardForm()
        return render(request, 'new.html', {'form': form})

    # request.session['title'] = str(title)
    # request.session['body'] = str(body)
    # request.session['created_at'] = str(created_at)
    # request.session['photo'] = photo

    return redirect('board')
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

    request.session['user'] = nickName
    request.session['profile'] = thumbnailURL
    # board = Board()
    # board.title = request.session.get('title')
    # board.body = request.session.get('body')
    # board.user = nickName
    # board.created_at = request.session.get('created_at')
    # board.photo = request.FILES('photo')
    # board.save()

    # form = BoardForm()

    # return render(request, 'new.html', {'form': form})
    return redirect('create')


# 동아리 홍보
def boothPromotion(request):
    boards_list = PromotionBoard.objects.all().order_by('-created_at')
    paginator = Paginator(boards_list, 6)  # 게시물 5개를 기준으로 페이지네이션 전개
    page = request.GET.get('page', 1)  # request 된 페이지를 변수에 담음
    posts = paginator.get_page(page)
    page_range = 5  # 5개의 페이지 블럭 (범위)
    current_block = math.ceil(int(page) / page_range)
    start_block = (current_block - 1) * page_range
    end_block = start_block + page_range
    p_range = paginator.page_range[start_block:end_block]

    return render(request, 'boards/boothPromotion.html', {'posts': posts, 'p_range': p_range})


# 술 친구
def friends(request):

    boards_list = FriendsBoard.objects.all().order_by('-created_at')
    paginator = Paginator(boards_list, 6)  # 게시물 5개를 기준으로 페이지네이션 전개
    page = request.GET.get('page', 1)  # request 된 페이지를 변수에 담음
    posts = paginator.get_page(page)
    page_range = 5  # 5개의 페이지 블럭 (범위)
    current_block = math.ceil(int(page) / page_range)
    start_block = (current_block - 1) * page_range
    end_block = start_block + page_range
    p_range = paginator.page_range[start_block:end_block]

    return render(request, 'boards/friends.html', {'posts': posts, 'p_range': p_range})
