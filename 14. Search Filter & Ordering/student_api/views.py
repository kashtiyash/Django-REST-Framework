from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter


class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    # search_fields = ['name', 'city', 'passBy']
    search_fields = ['^name']  # ^ means starts with

    ordering_fields = ['name']
    # ordering_fields = "__all__"
    # ordering_fields = ['name', 'passBy']
