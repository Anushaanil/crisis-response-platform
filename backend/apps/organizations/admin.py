from django.contrib import admin
from apps.organizations.models import Organization, Location

# Register your models here.
admin.site.register(Organization)
admin.site.register(Location)