from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from datetime import datetime

import random           ##랜덤하게 뒤섞기 위해 임포트

# Create your views here.
# request: 처음에 사용자의 요청 데이터
def index(request):             # 메소드를 정의 시 request라는 object를 받음
    now = datetime.now()
    context = {
        'current_date':now
    }                           # 삽입하기를 원하는 데이터들을 집어넣는 것
    return render(request, 'first/index.html',context)


def select(request):
    context = {}
    return render(request, 'first/select.html', context)


def result(request):
    chosen = int(request.GET['number'])             #숫자니까 반드시 int형으로 선언해주기

    results = []
    #만약 수가 범위를 초과하지 않으면 결과 값에 미리 선택한 수를 넣음
    if chosen >= 1 and chosen <= 45:
        results.append(chosen)

    #값을 꺼낼 박스 마련
    box = []
    for i in range(0,45):
        if chosen != i+1:
            box.append(i+1)

    #랜덤하게 섞는다.
    random.shuffle(box)
    #results 개수가 6개가 될 때까지 값을 하나씩 꺼냄
    while len(results) < 6:
        results.append(box.pop())

    context = {
        'numbers':results
    }
    return render(request, 'first/result.html', context)
