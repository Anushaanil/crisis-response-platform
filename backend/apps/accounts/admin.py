from django.contrib import admin
from apps.accounts.models import User, Role, Employee, Visitor

# Register your models here.
admin.site.register(User)
admin.site.register(Role)
admin.site.register(Employee)
admin.site.register(Visitor)