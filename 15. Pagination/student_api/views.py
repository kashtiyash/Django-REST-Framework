from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from .models import Student
from .serializers import StudentSerializer
from .CustomPagination import MyCursorPagination, MyLimitOffsetPagination


class StudentAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = PageNumberPagination
    # pagination_class = MyCursorPagination
    # pagination_class = MyLimitOffsetPagination
