"""project_farewell URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from videoApp.views import * # videoApp에 있는 모든 함수를 가져온다.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = "home"),                    # path('url 주소', views.py에 있는 함수명, name =  "namespace" html에서 접근가능한 이름 지정)
    path('main/',mainVideo, name = "mainVideo"),
    path('<str:id>', detailVideo, name="detailVideo"), # '<str:id>' 는 path converter
    path('new/',newVideo,name="newVideo"), 
    path('create/', createVideo, name="createVideo"),
    path('edit/<str:id>',editVideo, name = "editVideo"),
    path('update/<str:id>',updateVideo,name = "updateVideo"),
    path('delete/<str:id>', deleteVideo, name = "deleteVideo"),
]
