from django.db import models
from django.conf import settings


# Create your models here.
class Todo(models.Model):
    # db의 fk에는 user_id 라는 새 컬럼이 생김
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    


