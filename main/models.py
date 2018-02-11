from django.db import models
from django.contrib import admin

# Create your models here.
class Post(models.Model):
    article = models.CharField(max_length=200)
    user = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(auto_now=True)

class Option(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)
    hot_count = models.IntegerField(default=0)
    not_count = models.IntegerField(default=0)
