from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework import routers

# Creating a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register('student-api', views.StudentViewSet, basename='student-api')
router.register('model-view-set', views.StudentModelViewSet, basename='model-view-set')
router.register('readonly-model-view-set', views.StudentReadOnlyModelViewSet, basename='readonly-model-view-set')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

]
