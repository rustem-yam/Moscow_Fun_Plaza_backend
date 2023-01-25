from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ('name', 'email', 'password', 'liked_events', 'session_key')


class RegisterUserSerializer(serializers.ModelSerializer):
  email = serializers.CharField(max_length=254)

  class Meta:
    model = CustomUser
    fields = ('email', 'name', 'password')


class LoginUserSerializer(serializers.ModelSerializer):
  email = serializers.CharField(max_length=254)

  class Meta:
    model = CustomUser
    fields = ('email', 'password',)
