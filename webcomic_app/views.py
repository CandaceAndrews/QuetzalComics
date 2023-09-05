from django.shortcuts import render
from .models import Chapter, Comment


def chapter_detail(request, chapter_id):
    chapter = Chapter.objects.get(pk=chapter_id)
    comments = Comment.objects.filter(chapter=chapter)
    return render(request, 'webcomic/chapter_detail.html', {'chapter': chapter, 'comments': comments})
