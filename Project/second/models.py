from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)     #String형(길이 30)
    content = models.TextField()                #문자열 길이 정의X(긴 문자열)

    created_at = models.DateTimeField(auto_now_add=True)    #현재시간 기록
    updated_at = models.DateTimeField(auto_now=True)    #최근 수정일

    # num_stars = models.IntegerField()   # 숫자형


