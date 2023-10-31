from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import Chapter, Comment, Series
from .serializers import SeriesSerializer


@api_view(['GET'])
def api_root(request):
    # Implement the behavior for the api_root view
    # This can be a simple response with links to various API endpoints
    data = {
        "series": "/api/series/",
        "chapters": "/api/chapters/",
    }
    return Response(data)


class SeriesDetailView(generics.RetrieveAPIView):
    '''view details for single Series
    '''
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
