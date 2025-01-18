from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model


User = get_user_model()


class SignupSerializer(ModelSerializer):
    roles = serializers.CharField(source="role", read_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "nickname", "roles"]

        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            nickname=validated_data["nickname"],
        )
        return user

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {
            "username": representation["username"],
            "nickname": representation["nickname"],
            "roles": [{"role": representation["roles"]}],
        }
