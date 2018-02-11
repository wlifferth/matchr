from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .models import Post, Option
import json

# Create your views here.

def home(request):
    context = {}
    return render(request, 'main/home.html', {})

def feed(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'main/feed.html', context)

def post(request, post_id):
    post = Post.objects.filter(id=post_id).get()
    first_option = post.option_set.first()
    context = {'post': post, 'option': first_option}
    return render(request, 'main/post.html', context)

def vote(request, post_id, option_id, hot):
    print("HEYYY")
    post = Post.objects.filter(id=post_id).get()
    options = list(post.option_set.all())
    option = post.option_set.filter(id=option_id).get()
    response = {}
    if vote:
        option.hot_count += 1
    else:
        option.not_count += 1
    option.save()
    next_option_index = options.index(option) + 1
    if next_option_index >= len(options):
        response = {'end': True}
        return HttpResponse(json.dumps(response))
        # Return end of thing
    next_option = options[next_option_index]
    response['end'] = False
    response['hotURL'] = reverse('vote', kwargs={'post_id': post_id, 'option_id': next_option.id, 'hot': 1})
    response['notURL'] = reverse('vote', kwargs={'post_id': post_id, 'option_id': next_option.id, 'hot': 0})
    response['optionURL'] = next_option.url
    print(response)
    return HttpResponse(json.dumps(response))

def results(request, user):
    posts = Post.objects.filter(user=user)
    for post in posts:
        first_option = post.option_set.first()
        post.total = first_option.hot_count + first_option.not_count
    context = {'posts': posts, 'user': user}
    return render(request, 'main/results.html', context)

def result(request, user, post_id):
    context = {}
    post = Post.objects.filter(id=post_id).get()
    options = post.option_set.all()
    context['post'] = post
    context['options'] = options
    return render(request, 'main/result.html', context)

def new(request):
    context = {}
    return render(request, 'main/new.html', context)
