from django.db import models


class Organization(models.Model):
    name = models.CharField()
    domain = models.CharField()
    code = models.CharField()
    industry = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Location(models.Model):
    name = models.CharField()
    organization = models.ForeignKey(
        Organization,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    country = models.CharField()
    city = models.CharField()
    latitude = models.CharField()
    longitude = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name