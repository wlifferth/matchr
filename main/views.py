from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Option

# Create your views here.

def home(request):
    context = {}
    return render(request, 'main/home.html', {})

def feed(request):
    posts = Post.objects.all()
    for post in posts:
        print(dir(post))
    context = {'posts': posts}
    return render(request, 'main/feed.html', context)

def post(request, post_id):
    post = Post.objects.filter(id=post_id)
    print(post)
    return HttpResponse("Yo")

def results(request):
    context = {}
    return render(request, 'main/results.html', context)

def new(request):
    context = {}
    return render(request, 'main/new.html', context)
