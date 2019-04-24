from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts =    Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def index(request):
    return render(request, 'blog/index.html')
def reg(request):
    return render(request, 'blog/reg.html')
def login(request):
    return render(request, 'blog/login.html')
def about(request):
    return render(request, 'blog/about_us.html')
def archive(request):
    return render(request, 'blog/archive.html')
def contacts(request):
    return render(request, 'blog/contacts.html')
def working(request):
    return render(request, 'blog/working.html')
