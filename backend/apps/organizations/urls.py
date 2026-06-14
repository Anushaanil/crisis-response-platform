from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.organizations.views import (
    OrganizationViewSet,
    LocationViewSet
)

router = DefaultRouter()
router.register(r"organization", OrganizationViewSet, basename="organization"),
router.register(r"location", LocationViewSet, basename="location"),


urlpatterns = [
    path("", include(router.urls)),
]
    