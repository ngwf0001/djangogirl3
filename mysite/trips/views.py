from django.shortcuts import render
import datetime as dt
from .models import Post


# Create your views here.
from django.http import HttpResponse

def hello_world(request):
    return render(request, 'hello.html', {'current_time': dt.datetime.now})

def home(request):
    post_list = Post.objects.all()
    return render(request, 'home.html', {'post_list': post_list})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})
