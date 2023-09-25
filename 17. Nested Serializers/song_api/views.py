from django.shortcuts import render
from .models import Singer, Album
from .serializers import SingerSerializer, AlbumSerializer
from rest_framework import viewsets
# Create your views here.


class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

