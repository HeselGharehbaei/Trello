from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS,
)


class IsOwnerOrReadOnlyInUserDetail(BasePermission):
    message = 'permission denied, you are not the owner'

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method == 'POST':
            return request.user != request.user.is_authenticated
        
    def has_object_permission(self, request, view, obj):
        if request.method is SAFE_METHODS:
            return True
        return obj == request.user