# apps/accounts/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from config.permissions import IsSuperAdmin

from .serializers import (
    RegisterSerializer,
    UserSerializer
)


class HealthCheckView(APIView):
    # authentication_classes = [] we will authenticate with JWT
    permission_classes = [IsSuperAdmin]

    def get(self, request):
        return Response({"status": "ok"})


class RegisterView(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = RegisterSerializer


class LoginView(TokenObtainPairView):
    pass


class MeView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)

        return Response(serializer.data)


class LogOutView(APIView):
    def post(self, request):
        refresh_token = request.data.get("refresh_token")
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"message": "logged out successfully."})
