from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class RoleSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["role"]


class SignupSerializer(ModelSerializer):
    roles = RoleSerializer(read_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "nickname", "roles"]

        write_only_fields = ("password",)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            nickname=validated_data["nickname"],
        )

        return user
