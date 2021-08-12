from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404, redirect         
from django.utils import timezone        #pub_date를 위해 import
from .models import Blog           # models.py의 blog와 Blog에서 import받음
from .forms import BlogForm

def mainBlog(request):
    blogs = Blog.objects.all()
    return render(request,'main_blog.html',{'blogs' : blogs})

def detailBlog(request,id):                                         #영상 1개 보여주는 디테일 페이지
    blog = get_object_or_404(Blog, pk = id)   
    blogs = Blog.objects.all()                     # models.py에서 blog를 가져와서 blog에 넣음
    return render(request,'detail_blog.html',{'blog':blog, 'blogs':blogs})       # detail_blog.html로 blog를 보내줌

def newBlog(request):
    return render(request,'new_blog.html')


def createBlog(request):         
     new_blog = Blog()                             # blog 의 새로운 객체를 new_blog로 만들기      
     new_blog.title = request.POST['title']         # new_blog.html에서 작성한 제목을 new_blog.title에 할당
     new_blog.writer =request.POST['writer']
     new_blog.body = request.POST['body']
     new_blog.pub_date = timezone.now()             # 작성한 시간을  new_blog.pub_date에 할당
     new_blog.save()                                # 위의 내용들을 DB에 저장해주는 함수
     return redirect('detailBlog', new_blog.id)   # detailBlog로 돌아감 

def editBlog(request,id) :
    edit_blog = Blog.objects.get(id=id)                           # id값에 해당하는 blog 객체 하나 가져와서 edit_blog에 할당
    return render(request,'edit_blog.html',{'blog' : edit_blog}) # edit_blog.html에 키값을 blog로 설정한 edit_blog를 보냄
    
def updateBlog(request,id) : 
    update_blog = Blog.objects.get(id=id)            # id값에 해당하는 blog 객체 하나 가져와서 update_blog 에 할당                  
    update_blog.title = request.POST['title']        
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now()             
    update_blog.save()                                # 위의 내용들을 DB에 저장해주는 함수
    return redirect('detailBlog', update_blog.id)     # detailBlog로 돌아감 


def deleteBlog(request,id) : 
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')                       # home이 아닌 mainblog로 돌아감 : 비디오 메인페이지로 돌아감 <- 홈으로 수정해야할 수도 있음

