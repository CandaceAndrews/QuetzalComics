from django.contrib import admin
from .models import Chapter, Comment, Series


admin.site.register(Series)
admin.site.register(Chapter)
admin.site.register(Comment)
