from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Chapter(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='chapter_images/')
    summary = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
