from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

class AuthenticationHomeView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        return Response({
            'register' : reverse('register', request = request),
            'login' : reverse('login', request = request)
        })

class Register(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        return Response({
            'message' : 'To create an account, pass the credentials'
        })
    
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        if not serializer.is_valid():
            raise serializer.errors
        new_user = User.objects.create_user(username = serializer.validated_data.get('username'),
                                            password = serializer.validated_data.get('password'))
        refresh = RefreshToken.for_user(user = new_user)
        return Response({
            'message' : 'Account successfully created!',
            'access_token' : str(refresh.access_token),
            'refresh_token' : str(refresh)
        })

class Login(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        return Response({
            'message' : "To login, pass the account's credentials"
        })
    
    def post(self, request):
        credentials = LoginSerializer(data = request.data)
        user = authenticate(username = credentials.validated_data.get('username'),
                            password = credentials.validated_data.get('password'))
        if not user:
            raise AuthenticationFailed('Make sure to pass correct credentials!') 
        refresh = RefreshToken.for_user(user = user)
        return Response({
            'message' : 'Successfully authenticated the user!',
            'access_token' : str(refresh.access_token),
            'refresh_token' : str(refresh)
        })


class Logout(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        pass
    
    def post(self, request):
        pass    