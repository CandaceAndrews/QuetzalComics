from django.db import models
from users.models import User


class Series(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='series_covers/')
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='series_created')
    followers = models.ManyToManyField(
        User, related_name='series_followed', blank=True)

    def __str__(self) -> str:
        return self.title


class Chapter(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='chapter_images/')
    summary = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, default=None)

    def __str__(self) -> str:
        return f"{self.series} - {self.title}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
