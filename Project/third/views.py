from django.shortcuts import render,get_object_or_404
from third.models import Restaurant
from django.core.paginator import Paginator

from third.forms import RestaurantForm
from django.http import HttpResponseRedirect


# Create your views here.
def list(request):
    restaurants = Restaurant.objects.all()
    paginator = Paginator(restaurants, 5)   #한 페이지에 몇 개씩 보여줄지

    page = request.GET.get('page')   ## third/list?page=1 (query에서 page 데이터 가져옴)
    items = paginator.get_page(page)    ## 해당 페이지의 아이템으로 필터링

    context = {         #list
        'restaurants':items
    }
    return render(request, 'third/list.html',context)


def create(request):
    if request.method == "POST":
        form = RestaurantForm(request.POST) #request의 POST 데이터를 바로 POSTFORM에 담기
        if form.is_valid():
            new_item = form.save()          #save로 입력 받은 데이터를 바로 db에 저장함
        return HttpResponseRedirect('/third/list/')

    form = RestaurantForm()           #만약 post가 아니라면, 일반적인 폼 생성해서 render
    return render(request, 'third/create.html', {'form': form})


def update(request):
    if request.method == "POST" and 'id' in request.POST:   #id 없으면 return 되도록
        #item = Restaurant.objects.all(pk=request.GET.get('id')) #pk==id
        item = get_object_or_404(Restaurant, pk=request.POST.get('id')) ##
        form = RestaurantForm(request.POST, instance=item)  #여기에는 수정할 폼 초기화
        if form.is_valid():
            item = form.save()
    elif request.method == "GET":
        #item = Restaurant.objects.get(pk=request.GET.get('id')) #id가 지정되에서 들어옴(third/update?id=2)
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))  ##
        form = RestaurantForm(instance = item)
        return render(request, 'third/update.html', {'form': form})

    return HttpResponseRedirect('/third/list/')                     #리스트 화면으로 이동


def detail(request):
    if 'id' in request.GET:
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        return render(request, 'third/detail.html', {'item': item})

    return HttpResponseRedirect('/third/list/')


def delete(request):
    if 'id' in request.GET:
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        item.delete()

    return HttpResponseRedirect('/third/list/')