from django.shortcuts import render
from django.http import HttpResponse
from .models import Chapter, Comment


def home(request):
    return HttpResponse('<h1>QuetzalComics</h1>')


def chapter_detail(request, chapter_id):
    chapter = Chapter.objects.get(pk=chapter_id)
    comments = Comment.objects.filter(chapter=chapter)
    return render(request, 'webcomic/chapter_detail.html', {'chapter': chapter, 'comments': comments})
