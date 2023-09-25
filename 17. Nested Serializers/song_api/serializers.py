from .models import Singer, Album
from rest_framework import serializers


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'title', 'duration', 'singer']


class SingerSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)
    class Meta:
        model = Singer
        fields = ['id', 'name', 'nationality', 'albums']



