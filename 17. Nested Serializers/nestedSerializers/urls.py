from django.contrib import admin
from django.urls import path, include
from song_api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'singer', views.SingerViewSet)
router.register(r'album', views.AlbumViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]
