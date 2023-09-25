from django.contrib import admin
from .models import Singer, Album
# Register your models here.


@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'nationality')


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'singer', 'duration')
