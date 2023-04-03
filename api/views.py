from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Show, ShowInfo
from api.serializers import ShowSerializer

def index(request):
    return HttpResponse('Hello, DRF')


@api_view(['GET', 'POST'])
def show_list(request):
    if request.method == "GET":
        shows = Show.objects.all()
        return Response({'data': ShowSerializer(shows, many=True).data})

