from django.shortcuts import render

# Create your views here.
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    # check before getting to the api endpoint
    permission_classes = [IsAuthenticated]

    # permission_classes = [AllowAny]
    # allows access to all persons

    # allowed only to admin users
    # permission_classes = [IsAdminUser]

    # https: // www.django - rest - framework.org / api - guide / permissions /

