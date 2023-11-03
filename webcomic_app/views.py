from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from django.shortcuts import get_object_or_404
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


class SeriesByTagsListView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        # Get a comma-separated list of tag names from the query parameter 'tags'
        tag_names = request.GET.get('tags', '').split(',')

        # Filter series that have all the specified tags
        series = Series.objects.all()
        for tag_name in tag_names:
            series = series.filter(tags__name=tag_name)

        if not series:
            # No series found with the specified tags
            return Response({"detail": "No series found with the specified tags."}, status=404)

        serializer = SeriesSerializer(series, many=True)
        return Response(serializer.data)
