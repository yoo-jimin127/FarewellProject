from django.shortcuts import render,get_object_or_404, redirect         
from django.utils import timezone        #pub_date를 위해 import
from .models import Video
from blogApp.models import Blog           # models.py의 video에서 import받음 + blogApp의 models.py에서 import 받음
from .forms import VideoForm             #forms.py import

def home(request):
    videos = Video.objects.all()
    blogs = Blog.objects.all()                                     # models.py의 Video를 가져와서 videos에 넣음 + Blog
    return render(request,'home.html',{'videos' : videos, 'blogs' : blogs})           # home.html을 랜더링


def mainVideo(request):
    videos = Video.objects.all()
    return render(request,'main_video.html',{'videos' : videos})


def detailVideo(request,id):                                         #영상 1개 보여주는 디테일 페이지
    video = get_object_or_404(Video, pk = id)                        # models.py에서 Video를 가져와서 video에 넣음
    videos = Video.objects.all()
    return render(request,'detail_video.html',{'video':video, 'videos':videos})       # detail_video.html로 video를 보내줌


def newVideo(request):
    form = VideoForm()
    return render(request,'new_video.html', {'form':form})


def createVideo(request):                           # new_video.html에서 작성한 것들의 정보를 받음    
    form = VideoForm(request.POST, request.FILES)
    if form.is_valid(): # form의 유효성 검사
        new_video = form.save(commit=False) # new_video에 그 값을 임시 저장
        new_video.pub_date = timezone.now() # pub_date 따로 받음
        new_video.save()    # 저장
        return redirect('detailVideo', new_video.id) #유효할 경우 detailVideo로 이동
    return redirect('home') #유효하지 않을 경우 home으로 이동

    # new_video = Video()                             # Video 의 새로운 객체를 new_video로 만들기      
    # new_video.image = request.FILES['image']              
    # new_video.title = request.POST['title']         # new_video.html에서 작성한 제목을 new_video.title에 할당
    # new_video.writer =request.POST['writer']
    # new_video.youtube =request.POST['youtube']
    # new_video.pub_date = timezone.now()             # 작성한 시간을  new_video.pub_date에 할당
    # new_video.save()                                # 위의 내용들을 DB에 저장해주는 함수
    # return redirect('detailVideo', new_video.id)   # detailVideo로 돌아감 


def editVideo(request,id) :
    edit_video = Video.objects.get(id=id)                           # id값에 해당하는 Video 객체 하나 가져와서 edit_video에 할당
    return render(request,'edit_video.html',{'video' : edit_video}) # edit_video.html에 키값을 video로 설정한 edit_video를 보냄


def updateVideo(request,id) : 
    update_video = Video.objects.get(id=id)            # id값에 해당하는 Video 객체 하나 가져와서 update_video 에 할당                  
    update_video.title = request.POST['title']        
    update_video.writer = request.POST['writer']
    update_video.youtube = request.POST['youtube']
    update_video.pub_date = timezone.now()             
    update_video.save()                                # 위의 내용들을 DB에 저장해주는 함수
    return redirect('detailVideo', update_video.id)     # detailVideo로 돌아감 

def deleteVideo(request,id) : 
    delete_video = Video.objects.get(id=id)
    delete_video.delete()
    return redirect('home')                       # home이 아닌 mainVideo로 돌아감 : 비디오 메인페이지로 돌아감 <- 홈으로 수정해야할 수도 있음


