from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS,
)


class IsOwnerOrReadOnlyInBoard(BasePermission):
    message = 'permission denied, you are not the owner'

    def has_object_permission(self, request, view, obj):
        if request.method is SAFE_METHODS:
            return True
        return obj.owner == request.user
    

class IsOwnerOrReadOnlyInList(BaseException):
    message = 'permission denied, you are not the owner'

    def has_object_permission(self, request, view, obj):
        if request.method is SAFE_METHODS:
            return True
        return obj.board.owner == request.user
    

class IsOwnerOrReadOnlyInTask(BaseException):
    message = 'permission denied, you are not the owner'

    def has_object_permission(self, request, view, obj):
        if request.method is SAFE_METHODS:
            return True
        return obj.user == request.user
    

class IsOwnerOrReadOnlyInLabel(BaseException):
    message = 'permission denied, you are not the owner'

    def has_object_permission(self, request, view, obj):
        if request.mothed is SAFE_METHODS:
            return True
        return obj.board.owner == request.user
       