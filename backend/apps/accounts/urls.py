# apps/accounts/urls.py

from django.urls import path
from .views import (
    HealthCheckView,
    RegisterView,
    LoginView,
    MeView
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("health/", HealthCheckView.as_view(), name="health"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("refresh_token/", TokenRefreshView.as_view(), name="refresh_token"),
    path("me/", MeView.as_view())
]