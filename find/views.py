from django.shortcuts import render,redirect
from .models import Lost
from .forms import NewLost
from django.utils import timezone

# Create your views here.

def lost(request):
    losts = Lost.objects.filter(created_at__lte=timezone.now()).order_by('-created_at') # 최신 게시글순으로 정렬
    return render(request,'lost.html',{'losts':losts})   #분실물 찾기로 저장되는 함수

def newlost(request):                                    #분실물 등록 하는 함수 (구현못함)
    if request.method =='POST':
        forms = NewLost(request.POST,request.FILES) 
        if forms.is_valid():
            post=forms.save(commit=False)
            user = request.user.username
            post.user = user
            post.save()                   
            return redirect('lost')
    else:
        forms = NewLost()
        return render(request,'register.html', {'forms':forms})