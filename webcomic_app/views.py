from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .models import Chapter, Comment


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            ""
        }
    )
