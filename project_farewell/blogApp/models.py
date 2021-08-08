from django.db import models

# videoApp 의 models.py에 blogApp도 같이 구현
class Blog(models.Model) :
    title = models.CharField(max_length=200)         # 제목
    writer = models.CharField(max_length=100)        # 작성자
    pub_date = models.DateTimeField()                # 게시물 올린 날짜
    body = models.TextField()   #게시물의 내용

    def __str__(self):
        return self.title # 글의 제목으로 볼 수 있게 만들어줌

    def summary(self):
        return self.body[:100]  # 100자만 볼 수 있도록 설정