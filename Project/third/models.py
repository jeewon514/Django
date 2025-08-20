from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)            # 넣어주는 것이 좋음(현재 시간 기록)
    updated_at = models.DateTimeField(auto_now=True)                # 넣어주는 것이 좋음(최근 수정일)

class Review(models.Model):
    point = models.IntegerField()
    comment = models.CharField(max_length=500)
    #review는 레스토랑에 딸려있는 것
    # "on_delete=models.CASCADE" 로 지정하면 식당이 삭제되면 같이 삭제됨
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)