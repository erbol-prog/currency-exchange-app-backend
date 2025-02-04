from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'

class IsCashierOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and 
                (request.user.role == 'admin' or request.user.role == 'cashier'))


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Разрешаем GET (list/retrieve) всем аутентифицированным
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated
        # POST, PUT, DELETE - только если роль admin
        return (request.user.is_authenticated and request.user.role == 'admin')

