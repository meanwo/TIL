from django.shortcuts import render, redirect
from .models import Article

# 메인 화면
# views -> templates 데이터 전송 학습
# index.html 로 데이터 전달
def index(request):
    name = "정민우"
    lunchs = ['된장전골', '오리고기', '라면']
    word = 'SSAFY'
    long_word = "스며들어 소리다.이것은 할지니, 위하여서. 눈이 위하여 이상 따뜻한 봄바람이다. 기관과 기쁘며, 주는 오아이스도 밝은 꽃이 가치를 것이다. 길을 가진 있음으로써 갑 보이는 인도하겠다는 주며, 길지 그리하였는가? 할지라도 이상의 피어나는 때문이다. 이성은 같은 인생을 우리는 얼마나 사막이다. 가슴에 자신과 사람은 찾아 목숨이 말이다. 우리 그러므로 광야에서 뿐이다. 이것은 봄날의 그것은 칼이다."
    flag = 2

    context = {
        'name': name,
        'lunchs': lunchs,
        'word': word,
        'longword': long_word,
        'flag': flag,
    }

    return render(request, 'articles/index.html', context)


# 상속 학습
def inherit(request):
    return render(request, 'articles/inherit.html')


# 데이터 전송 학습
def throw(request):
    return render(request, 'articles/throw.html')


# 전송된 데이터를 받음
# request 객체 내부에 요청 시 보낸 데이터가 모두 들어가 있음
# thorw 에서 GET method 를 통해서 보냈으므로,
#   request.GET.get() 을 통해서 접근
def catch(request):
    # raise
    # print(request.GET.get('message'))

    message = request.POST.get('message')

    context = {
        'message': message,
    }

    return render(request, 'articles/catch.html', context)


# Variable routing 학습
# urls.py 의 꺽쇠괄호 안에 작성된 변수를 2번째 파라미터로 받음
# 해당 name 을 그대로 hello.html 로 전송
def hello(request, name):
    context = {
        'name': name,
    }

    return render(request, 'articles/hello.html', context)

def main(request):
  articles = Article.objects.all()
  
  context = {
    'articles': articles,
  }

  return render(request, 'articles/main.html', context)

def new(request):
  return render(request, 'articles/new.html')


def create(request):
  title = request.POST.get('title')
  content = request.POST.get('content')



  article = Article(title=title, content=content)
  article.save()
  return redirect('articles:main')

def detail(request, pk):
  article = Article.objects.get(pk=pk)
  context = {
    'article': article,
  }
  return render(request, 'articles/detail.html', context)

def delete(request, pk):
  article = Article.objects.get(pk=pk)
  article.delete()
  return redirect('articles:main')

def edit(request, pk):
  article = Article.objects.get(pk=pk)
  context = {
    'article' : article,
  }
  return render(request, 'articles/edit.html', context)

def update(request,pk):
  article = Article.objects.get(pk=pk)
  article.title = request.POST.get('title')
  article.content = request.POST.get('content')
  article.save()
  return redirect('articles:detail', article.pk)
  