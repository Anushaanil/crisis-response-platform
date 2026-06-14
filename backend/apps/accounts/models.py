from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.organizations.models import Organization, Location


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    

class User(AbstractUser):
    first_name = models.CharField()
    last_name = models.CharField()
    email = models.EmailField(unique=True)
    role = models.ForeignKey(
        Role,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email


class Employee(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    designation = models.CharField()
    department = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Visitor(models.Model):
    name = models.CharField()
    email = models.EmailField()
    phone = models.SmallIntegerField()
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
