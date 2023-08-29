from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS,
)


class IsOwnerOrReadOnlyInUserDetail(BasePermission):
    message = 'permission denied, you are not the owner'

    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.is_authenticated
        if view.action == 'create':
            return  request.user.is_authenticated == False
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if view.action in ['list', 'create']:
            return True
        return obj == request.user
    