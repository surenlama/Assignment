from django.contrib.auth.models import User
from rest_framework import serializers


class UserCreateSerialzier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "email",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(username=validated_data["username"], email=validated_data["email"])
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserListSerialzier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
        )