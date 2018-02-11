from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('feed', views.feed, name='feed'),
    path('results/<user>', views.results, name='results'),
    path('results/<user>/<int:post_id>', views.result, name='result'),
    path('new', views.new, name='new'),
    path('post/<int:post_id>', views.post, name='post'),
    path('vote/<int:post_id>/<int:option_id>/<int:hot>', views.vote, name='vote'),
]
