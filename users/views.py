from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import User


class UserDetailView(generics.RetrieveAPIView):
    ''' view details for single user
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
