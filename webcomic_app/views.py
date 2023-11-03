from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from django.shortcuts import get_object_or_404
from django.db.models import Q
from taggit.models import Tag

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


class SeriesSearchView(APIView):
    '''Search for series with the specified tags
    '''

    def get(self, request):
        # Get the tags from the query parameters
        tags = request.GET.getlist('tags')

        series = Series.objects.filter(tags__name__in=tags).distinct()

        serializer = SeriesSerializer(series, many=True)

        # Return the serialized data in a JSON response
        return Response(serializer.data)
