from django.contrib import admin
from django.urls import path
from student_api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_api/', views.StudentAPIView.as_view(), name='student_list'),
]
