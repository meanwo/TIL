
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('inherit/', views.inherit, name='inherit'),
    # url을 받으면 views의 throw로 전송한다는 의미
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<str:name>/', views.hello, name='hello'),
    
]
