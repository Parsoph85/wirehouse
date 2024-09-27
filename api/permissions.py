from rest_framework import permissions


class IsSupplyer(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return request.user_type


class IsSupply(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == True


class IsConsumer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == False
