from django.urls import path, re_path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('select/', views.select, name='select'),
    path('result/', views.result, name='result'),
]