from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import (IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly,
                                        DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]

    # permission_classes = [IsAuthenticated]  # Only Authenticated users have access

    # permission_classes = [IsAdminUser]  # Only Staff users have access

    # permission_classes = [AllowAny]  # Any users have access

    # permission_classes = [IsAuthenticatedOrReadOnly]
    # Only Authenticated users have read and write permissions and unauthenticated users have only read permissions

    # permission_classes = [DjangoModelPermissions]
    # User must be authenticated: default get permission is allowed but we have to assign permission user
    # such as add, update, delete

    permission_classes = [
        DjangoModelPermissionsOrAnonReadOnly]  # Similar to DjangoModelPermissions but allows unauthenticated users ## to have read-only permissions
