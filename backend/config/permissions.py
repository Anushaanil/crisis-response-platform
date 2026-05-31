from rest_framework.permissions import BasePermission


class IsSuperAdmin(BasePermission):

    def has_permission(self, request, view):
        print(request.user.is_authenticated)
        print(request.user)
        
        return (
            request.user.is_authenticated
            and request.user.role.name == "SUPER_ADMIN"
        )