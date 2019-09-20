from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
# from .models import Comment, Board, BoothPromotionBoard, FriendsBoard, FreeBoard
from .models import Comment, Board, FriendsBoard
# from .forms import CommentForm, BoardForm, BoothPromotionForm, FriendsForm, FreeForm
from .forms import CommentForm, BoardForm, FriendsForm
from django.core.paginator import Paginator
import requests, math

# Create your views here.

def home(request):
    comments = Comment.objects.all()
    boards_list = Board.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'comments':comments, 'boards_list':boards_list})

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


# primary key 값을 부여해서 게시글 마다 고유한 번호를 가질수 있게 설계 (게시글 구분)
def detail(request, board_id):
    board_detail = get_object_or_404(Board, pk=board_id)
    return render(request, 'boards/detail.html', {'board' : board_detail})


# 글쓰기 버튼
def new(request):

    login_request_uri = 'https://kauth.kakao.com/oauth/authorize?'

    client_id = 'd9079dbac88fca9754d091a7af0366ed'
    redirect_uri = 'http://127.0.0.1:8000/oauth'
    # redirect_uri = 'http://ec2-15-164-28-194.ap-northeast-2.compute.amazonaws.com:8000/oauth'

    login_request_uri += 'client_id=' + client_id
    login_request_uri += '&redirect_uri=' + redirect_uri
    login_request_uri += '&response_type=code'

    request.session['client_id'] = client_id
    request.session['redirect_uri'] = redirect_uri

    return redirect(login_request_uri)


# 제출 버튼을 누른뒤 작성한 게시글 detail로 보내기 위한 함수
def create(request):

    if request.method == 'POST':
        form = BoardForm(request.POST, request.FILES)

        if form.is_valid():

            post = form.save(commit=False)

            post.user = request.session.get('user')
            post.profile = request.session.get('profile')
            post.user_id = request.session.get('user_id')

            request.session['user'] = {}
            request.session['profile'] = {}
            request.session['user_id'] = {}
            request.session.modified = True

            post.save()

            return redirect('board')
        else:
            return redirect('board')
    else:
        form = BoardForm()
        return render(request, 'boards/new.html', {'form': form})

    return redirect('board')


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

    user_all_data_uri = "https://kapi.kakao.com/v2/user/me?access_token="
    user_all_data_uri += str(access_token)
    user_all_data_uri_data = requests.get(user_all_data_uri)
    user_all_json_data = user_all_data_uri_data.json()
    user_id = user_all_json_data['id']
    print(user_id)
    request.session['user_id'] = user_id

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

    if request.session.get('boothPromotionNew') == 'boothPromotionNew':

        request.session['boothPromotionNew'] = {}
        request.session.modified = True

        return redirect('boothPromotionCreate')

    elif request.session.get('friendsNew') == 'friendsNew':

        request.session['friendsNew'] = {}
        request.session.modified = True

        return redirect('friendsCreate')

    elif request.session.get('freeNew') == 'freeNew':

        request.session['freeNew'] = {}
        request.session.modified = True

        return redirect('freeCreate')
    else:
        request.session.modified = True
        return redirect('create')


# ################# 삭제 #################
# ########################
# ## 동아리 홍보 게시판 ##
# # 동아리 홍보 게시판 메인
# def boothPromotion(request):
#
#     boards_list = BoothPromotionBoard.objects.all().order_by('-created_at')
#     paginator = Paginator(boards_list, 5)  # 게시물 5개를 기준으로 페이지네이션 전개
#     page = request.GET.get('page', 1)  # request 된 페이지를 변수에 담음
#     posts = paginator.get_page(page)
#     page_range = 5  # 5개의 페이지 블럭 (범위)
#     current_block = math.ceil(int(page) / page_range)
#     start_block = (current_block - 1) * page_range
#     end_block = start_block + page_range
#     p_range = paginator.page_range[start_block:end_block]
#
#     return render(request, 'boards/boothPromotion/boothPromotion.html', {'posts': posts, 'p_range': p_range})
# ################# 삭제 #################
#
#
# ################# 삭제 #################
# def boothPromotionDetail(request, board_id):
#     board_detail = get_object_or_404(BoothPromotionBoard, pk=board_id)
#     return render(request, 'boards/boothPromotion/boothPromotionDetail.html', {'board' : board_detail})
# ################# 삭제 #################
#
#
# ################# 삭제 #################
# # 부스 홍보 글쓰기 누르면
# def boothPromotionNew(request):
#     request.session['boothPromotionNew'] = str('boothPromotionNew')
#     return redirect('new')
# ################# 삭제 #################
#
#
# ################# 삭제 #################
# # 부스 홍보 입력 폼
# def boothPromotionCreate(request):
#
#     if request.method == 'POST':
#         form = BoothPromotionForm(request.POST, request.FILES)
#
#         if form.is_valid():
#
#             post = form.save(commit=False)
#
#             post.user = request.session.get('user')
#             post.profile = request.session.get('profile')
#
#             request.session['user'] = {}
#             request.session['profile'] = {}
#             request.session.modified = True
#
#             post.save()
#
#             return redirect('boothPromotion')
#         else:
#             return redirect('boothPromotion')
#     else:
#         form = BoothPromotionForm()
#         return render(request, 'boards/boothPromotion/boothPromotionNew.html', {'form': form})
#
#     return redirect('board')
# ################# 삭제 #################


########################
## 술 친구 홍보 게시판 ##
# 술 친구 게시판 메인
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

    return render(request, 'boards/friends/friends.html', {'posts': posts, 'p_range': p_range})


def friendsDetail(request, board_id):
    board_detail = get_object_or_404(FriendsBoard, pk=board_id)
    return render(request, 'boards/friends/friendsDetail.html', {'board' : board_detail})


# 술 친구 글쓰기 누르면
def friendsNew(request):
    request.session['friendsNew'] = str('friendsNew')
    return redirect('new')


# 술친구 입력 폼
def friendsCreate(request):

    if request.method == 'POST':
        form = FriendsForm(request.POST, request.FILES)

        if form.is_valid():

            post = form.save(commit=False)

            post.user = request.session.get('user')
            post.profile = request.session.get('profile')
            post.user_id = request.session.get('user_id')

            request.session['user'] = {}
            request.session['profile'] = {}
            request.session['user_id'] = {}
            request.session.modified = True

            post.save()

            return redirect('friends')
        else:
            return redirect('friends')
    else:
        form = FriendsForm()
        return render(request, 'boards/friends/friendsNew.html', {'form': form})

    return redirect('board')


# ################# 삭제 #################
# ########################
# ## 자유 게시판 ##
# # 자유 게시판 메인
# def free(request):
#
#     boards_list = FreeBoard.objects.all().order_by('-created_at')
#     paginator = Paginator(boards_list, 5)  # 게시물 5개를 기준으로 페이지네이션 전개
#     page = request.GET.get('page', 1)  # request 된 페이지를 변수에 담음
#     posts = paginator.get_page(page)
#     page_range = 5  # 5개의 페이지 블럭 (범위)
#     current_block = math.ceil(int(page) / page_range)
#     start_block = (current_block - 1) * page_range
#     end_block = start_block + page_range
#     p_range = paginator.page_range[start_block:end_block]
#
#     return render(request, 'boards/free/free.html', {'posts': posts, 'p_range': p_range})
# ################# 삭제 #################
#
#
# ################# 삭제 #################
# def freeDetail(request, board_id):
#     board_detail = get_object_or_404(FreeBoard, pk=board_id)
#     return render(request, 'boards/free/freeDetail.html', {'board' : board_detail})
# ################# 삭제 #################
#
#
# ################# 삭제 #################
# def freeNew(request):
#     request.session['freeNew'] = str('freeNew')
#     return redirect('new')
# ################# 삭제 #################
#
#
# ################# 삭제 #################
# def freeCreate(request):
#
#     if request.method == 'POST':
#         form = FreeForm(request.POST, request.FILES)
#
#         if form.is_valid():
#
#             post = form.save(commit=False)
#
#             post.user = request.session.get('user')
#             post.profile = request.session.get('profile')
#
#             request.session['user'] = {}
#             request.session['profile'] = {}
#             request.session.modified = True
#
#             post.save()
#
#             return redirect('free')
#         else:
#             return redirect('free')
#     else:
#         form = FreeForm()
#         return render(request, 'boards/free/freeNew.html', {'form': form})
#
#     return redirect('board')
# ################# 삭제 #################