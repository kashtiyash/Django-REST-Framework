from django.shortcuts import render
from .models import Student
from rest_framework import viewsets
from .serializers import StudentSerializer
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .customThrottling import CustomUserRateThrottle


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]  # Default Throttle rates are applied
    throttle_classes = [AnonRateThrottle, CustomUserRateThrottle]  # Custom Throttle rates are applied

# class StudentList(ListAPIView):
#     queryset = models.Student.objects.all()
#     serializer_class = serializers.StudentSerializer
#     throttle_classes = [ScopedRateThrottle]
#     throttle_scope = 'viewstudent'
#
#
# class StudentCreate(CreateAPIView):
#     queryset = models.Student.objects.all()
#     serializer_class = serializers.StudentSerializer
#     throttle_classes = [ScopedRateThrottle]
#     throttle_scope = 'poststudent'
#
#
# class StudentRetrieve(RetrieveAPIView):
#     queryset = models.Student.objects.all()
#     serializer_class = serializers.StudentSerializer
#     throttle_classes = [ScopedRateThrottle]
#     throttle_scope = 'viewstudent'
#
#
# class StudentUpdate(UpdateAPIView):
#     queryset = models.Student.objects.all()
#     serializer_class = serializers.StudentSerializer
#     throttle_classes = [ScopedRateThrottle]
#     throttle_scope = 'modifystudent'
#
#
# class StudentDestroy(DestroyAPIView):
#     queryset = models.Student.objects.all()
#     serializer_class = serializers.StudentSerializer
#     throttle_classes = [ScopedRateThrottle]
#     throttle_scope = 'modifystudent'
