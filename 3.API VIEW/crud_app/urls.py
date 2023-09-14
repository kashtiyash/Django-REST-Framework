from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("student/", views.student_api),
    path("student/<int:pk>", views.student_api),
    path("employee/", views.EmployeeAPIView.as_view()),
    path("employee/<int:pk>", views.EmployeeAPIView.as_view()),


]
