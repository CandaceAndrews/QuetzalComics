from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_root),
    path("series/<int:pk>/", views.SeriesDetailView.as_view(), name='series-detail'),
    path('series/tag/<str:tag_name>/',
         views.SeriesByTagListView.as_view(), name='series-by-tag')
]
