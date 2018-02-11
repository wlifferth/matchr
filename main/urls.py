from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('feed', views.feed, name='feed'),
    path('results', views.results, name='results'),
    path('new', views.new, name='new'),
    path('post/<post_id>', views.post, name='post'),
]
