from rest_framework import viewsets
from apps.organizations.models import (
    Organization, 
    Location
)
from apps.organizations.serializers import (
    OrganizationSerializer,
    LocationSerializer
)

class OrganizationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationSerializer
    model = Organization
    queryset = model.objects.all()


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    model = Location
    queryset = model.objects.all()