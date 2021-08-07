from django.db import models

# Create your models here.

class Video(models.Model) :
    title = models.CharField(max_length=200)         # 영상 제목
    writer = models.CharField(max_length=100)        # 영상 작성자
    youtube = models.CharField(max_length=100)       # 유튜브 공유 속성 중 다른 값
    pub_date = models.DateTimeField()                # 게시물 올린 날짜 
    image = models.ImageField(upload_to = "videoApp/", blank=True, null=True)   # 유튜브 영상 이미지

    def __str__(self):
        return self.title # 글의 제목으로 볼 수 있게 만들어줌