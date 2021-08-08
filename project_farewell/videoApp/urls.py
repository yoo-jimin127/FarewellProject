from django.contrib import admin
from django.urls import path
from .views import *

# videoApp 안에서의 url 관리를 위한 작업 (home과 admin 제외 타 기능)

urlpatterns = [
    path('main/',mainVideo, name = "mainVideo"),
    path('<str:id>', detailVideo, name="detailVideo"),
    path('new/', newVideo, name="newVideo"),
    path('create/', createVideo, name="createVideo"),
    path('edit/<str:id>', editVideo, name="editVideo"),
    path('update/<str:id>', updateVideo, name="updateVideo"),
    path('delete/<str:id>', deleteVideo, name="deleteVideo"),
  

]