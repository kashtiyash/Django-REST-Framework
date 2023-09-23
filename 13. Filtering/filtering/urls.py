from student_api import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_api/', views.StudentListView.as_view(), name='student_list'),
]
