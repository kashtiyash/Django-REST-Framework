from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['passBy']  # single filer model
    # filterset_fields = ['city', 'passBy'] #multiple filer model

    # override queryset to return only students that is passed by the current user
    # def get_queryset(self):
    #     user = self.request.user
    #     return Student.objects.filter(passBy=user)

