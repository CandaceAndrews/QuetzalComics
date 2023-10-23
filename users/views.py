from django.shortcuts import render
from .models import User


class UserDetailView(generics.RetrieveAPIView):
    ''' view details for single user
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
