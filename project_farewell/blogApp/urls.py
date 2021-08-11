from django.contrib import admin
from django.urls import path
from .views import *

# videoApp 안에서의 url 관리를 위한 작업 (home과 admin 제외 타 기능)

urlpatterns = [
    path('main/',mainBlog,name="mainBlog"),
    path('<str:id>', detailBlog, name="detailBlog"),
    path('new/', newBlog, name="newBlog"),
    path('create/', createBlog, name="createBlog"),
    path('edit/<str:id>', editBlog, name="editBlog"),
    path('update/<str:id>', updateBlog, name="updateBlog"),
    path('delete/<str:id>', deleteBlog, name="deleteBlog"),
    

]