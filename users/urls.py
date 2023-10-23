from django.urls import path
from users import views

urlpatterns = [
    path('users/<str:username>/', views.UserDetailView.as_view(), name='user-detail'),
]
