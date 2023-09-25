from .models import Singer, Album, Student
from rest_framework import serializers


class SingerSerializer(serializers.ModelSerializer):
    albums = serializers.StringRelatedField(many=True, read_only=True)
    # albums = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # albums = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='album-detail')
    # albums = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    # albums = serializers.HyperlinkedIdentityField(view_name='album-detail')

    class Meta:
        model = Singer
        fields = ['id', 'name', 'nationality', 'albums']


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'title', 'duration']


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'url', 'name', 'nationality']
        # we get url by default because of HyperlinkedModelSerializer
