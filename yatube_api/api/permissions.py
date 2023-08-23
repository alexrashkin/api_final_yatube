from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    # Разрешаем только владельцам поста редактировать и удалять его
    def has_object_permission(self, request, view, obj):
        if obj.author != request.user:
            return request.method in permissions.SAFE_METHODS

        return obj.author == request.user

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)
