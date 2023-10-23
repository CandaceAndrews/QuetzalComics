from django.urls import path
from users import views

urlpatterns = [
    path('user/<str:username>', UserDetailView.as_view(), name='user-detail'),
]
