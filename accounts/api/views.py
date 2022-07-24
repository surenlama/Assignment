from rest_framework.generics import CreateAPIView, GenericAPIView,ListAPIView
from django.contrib.auth.models import User
from accounts.api.serializers import (

    UserCreateSerialzier,
    UserListSerialzier

)

#Create user
class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerialzier

#View user
class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerialzier