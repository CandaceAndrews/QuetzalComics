from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chapter/<int:chapter_id>/', views.chapter_detail, name='chapter_detail'),
]
