from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import User, Profile
from .serializers import UserSerializer, ProfileSerializer


class UserDetailView(generics.RetrieveAPIView):
    ''' view details for single user
    '''
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


class ProfileDetailView(generics.RetrieveAPIView):
    ''' View details for a user's profile, including their username, profile image, and series created.
    '''
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_url_kwarg = 'username'
