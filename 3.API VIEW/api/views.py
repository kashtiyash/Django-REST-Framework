from rest_framework.decorators import api_view, APIView
# from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student, Employee
from .serializers import StudentSerializer, EmployeeSerializer


# -------------- Function Based api view ---------------------


@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def student_api(request, pk=None):
    if request.method == "GET":
        if pk:
            stu = Student.objects.get(id=pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data, )

    if request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "POST request successful"})

    if request.method == "PUT":
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "PUT request successful"})

    if request.method == "PATCH":
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Student Updated'})
        return Response(serializer.errors)

    if request.method == "DELETE":
        id = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({"message": "DELETE request successful"})


# --------------- class based api view ---------------------


class EmployeeAPIView(APIView):
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def get(self, request, pk=None):
        id = pk
        if id is not None:
            student = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(student)
            return Response(serializer.data)

        student = Employee.objects.all()
        serializer = EmployeeSerializer(student, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "POST request successful"})

    def put(self, request, pk=None):
        id = pk
        stu = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(stu, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "PUT request successful"})

    def patch(self, request, pk=None):
        id = pk
        stu = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Student Updated'})
        return Response(serializer.errors)

    def delete(self, request, pk=None):
        id = pk
        stu = Employee.objects.get(id=id)
        stu.delete()
        return Response({"message": "DELETE request successful"})

