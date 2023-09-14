from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.LCStudentAPIView.as_view()),
    path('studentapi/<int:pk>/', views.RUDStudentAPI.as_view()),

]
