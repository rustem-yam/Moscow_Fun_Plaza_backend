from rest_framework.views import APIView
from rest_framework import status, generics
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import login, authenticate, logout
# from django.shortcuts import redirect
from .serializers import UserSerializer, RegisterUserSerializer, LoginUserSerializer
from .models import CustomUser
from rest_framework.response import Response
import json


# Create your views here.
class RegisterUserView(APIView):
  serializer_class = RegisterUserSerializer

  def post(self, request, format=None):
    serializer = self.serializer_class(data=request.data)
    if not(serializer.is_valid()):
      return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
    
    email = serializer.data.get('email')
    name = serializer.data.get('name')
    password = serializer.data.get('password')

    emails = [self.serializer_class(user).data['email'] for user in CustomUser.objects.all()]

    if email in emails:
      return Response({'Reg Error': 'Email is not unique'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = CustomUser.objects.create_user(
      email=email,
      name=name,
      password=password,
    )

    login(request, user)

    return Response(self.serializer_class(user).data, status=status.HTTP_201_CREATED)


class LoginUserView(APIView):
  serializer_class = LoginUserSerializer
  def post(self, request, format=None):
    if request.user.is_authenticated:
      return Response({'Login Error': f'User {request.user} is already logged in'}, status=status.HTTP_423_LOCKED)
    serializer = self.serializer_class(data=request.data)
    if not(serializer.is_valid()):
      return Response({'Bad Request': 'Invalid data...',}, status=status.HTTP_400_BAD_REQUEST)
    
    email = serializer.data.get('email')
    password = serializer.data.get('password')

    user = authenticate(request, email=email, password=password)
    if user is None:
      return Response({'Login Error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)

    login(request, user)
    return Response({"Login Successfully": f'{user}'}, status=status.HTTP_202_ACCEPTED)

@method_decorator(csrf_exempt, name='dispatch')
class LogoutUserView(APIView):
  def post(self, request, format=None):
    logout(request)
    return Response({'Logout successfully'}, status=status.HTTP_200_OK)

