from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views import View
import io
from django.http import JsonResponse, HttpResponse
# Create your views here.


class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        print(json_data)
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        id = pythonData.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        json_data =request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        serializer = StudentSerializer(pythonData)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Student added successfully!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

