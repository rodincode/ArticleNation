from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):

    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=2000)
    title = models.CharField(max_length=30)
    likes = models.ManyToManyField(User,related_name='blogpost',default = 0)

    def numberoflikes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

        
