from django.urls import path
from users import views

urlpatterns = [
    path('user/<str:username>/', views.UserDetailView.as_view(), name='user-detail'),
    path('user/profile/<str:user__username>/',
         views.ProfileDetailView.as_view(), name='user-profile-detail')
]
