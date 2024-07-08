from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from users.models import User
from users.serializers import UserSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
