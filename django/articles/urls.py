# App URL mapping 이 된 후 이 파일이 생성됨
from django.urls import path
from . import views

# view 나 templates 에서 직접 url 을 사용하면 여러 단점들이 많음
#   수정 하면 다 수정해야 하는 등
# name 으로 URL 의 이름을 지정하여 사용

app_name = "articles"

urlpatterns = [
    path('index/', views.index, name='index'),
    path('inherit/', views.inherit, name='inherit'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<str:name>/', views.hello, name='hello'),
    # path('hello/<int:name>/', views.hello),
    path('main/', views.main, name='main'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),



]
