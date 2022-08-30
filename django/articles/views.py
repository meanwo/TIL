from django.shortcuts import render

# Create your views here.
def index(request):
  name = '정민우'

  lunchs = ['된장전골', '오리고기', '라면']
  word = 'SSAFY'
  longword = 'asdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdf'
  flag = 0
  context = {
    'name': name,
    'lunchs': lunchs,
    'word': word,
    'longword' : longword,
    'flag' : flag,
  }
  return render(request, 'index.html', context)

def inherit(request):
  return render(request, 'inherit.html')


def throw(request):
  return render(request, 'throw.html')

def catch(request):
  message = request.GET.get('message')
  context = {
    'message' : message
  }
  return render(request, 'catch.html',context)
def hello(request, name):
  context = {
    'name': name,

  }

  return render(request, 'hello.html', context)
  