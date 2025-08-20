from django.shortcuts import render
from django.http import HttpResponseRedirect

from second.models import Post
from . forms import PostForm        # 폼을 사용하기 위해서


# Create your views here.
def list(request):
    context = {
        'items':Post.objects.all()
    }
    return render(request,'second/list.html', context)


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)                   # post일 경우 POSTForm을 써서, request.POST로 처리
        if form.is_valid():                             # form 은 valid 하다
            #print(form)        ## 레코드를 생성하는 코드 필요(terminal에 출력)
            new_item = form.save()      # 폼에 입력한 것들이 모델 스키마에 자동으로 저장됨
        return HttpResponseRedirect('/second/list/')                # form이 valid 하지 않을 경우 (redirect 시키기)

    form = PostForm()
    # context를 따로 선언하지 않고 return에 바로 넣어주기
    return render(request, 'second/create.html', {'form':form})


def confirm(request):
    form = PostForm(request.POST)       # 우리가 원하는 데이터들의 맵핑이 끝남
    if form.is_valid():     # 유효성 검사
        return render(request,'second/confirm.html',{'form':form})
    # redirect: 다른 페이지에서 특정페이지로 이동
    # ( 만약 틀리면 다시 입력 폼으로 이동 -> create )
    return HttpResponseRedirect('/second/create/')
    
