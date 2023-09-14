from rest_framework.mixins import (ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin,
                                   RetrieveModelMixin)
from rest_framework.generics import GenericAPIView
from .models import Student
from .serializers import StudentSerializer


# List and create does not require pk ,so we can combine the two
class LCStudentAPIView(GenericAPIView, ListModelMixin, CreateModelMixin,):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# Retrieve ,delete and update do require pk,so we can combine them
class RUDStudentAPI(GenericAPIView, DestroyModelMixin, UpdateModelMixin, RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
