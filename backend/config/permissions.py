from rest_framework.permissions import BasePermission


class IsSuperAdmin(BasePermission):

    def has_permission(self, request, view):
        # print(request.user.is_authenticated)
        # print(request.user)
        
        return (
            request.user.is_authenticated
            and request.user.role.name == "SUPER_ADMIN"
        )

class IsOrgAdmin(BasePermission):

    def has_permission(self, request, view):
        
        return (
            request.user.is_authenticated
            and request.user.role.name == "ORG_ADMIN"
        )
    
class IsSecurityTeam(BasePermission):

    def has_permission(self, request, view):
        
        return (
            request.user.is_authenticated
            and request.user.role.name == "SECURITY_TEAM"
        )


class IsEmployee(BasePermission):

    def has_permission(self, request, view):
        
        return (
            request.user.is_authenticated
            and request.user.role.name == "EMPLOYEE"
        )


class IsVisitor(BasePermission):

    def has_permission(self, request, view):
        
        return (
            request.user.is_authenticated
            and request.user.role.name == "VISITOR"
        )