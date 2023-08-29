from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS,
)


class IsMemberBoardOrnot(BasePermission):
    massage = 'permission denied, you are not is the member of board'
    
    def has_object_permission(self, request, view, obj):
        if request.user == obj.workspace.member :
            return True
        return False 
    
# for comment member 
class IsMemberOfTheTask(BasePermission):
    massage = 'permission denied, you are not is the member of list'
    
    def has_object_permission(self, request, view, obj):
        if request.user == obj.task.user :
            return True
        return False


class IsOwnerOrReadOnlyInBoard(BasePermission):
    message = 'permission denied, you are not the owner'
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user

    def has_object_permission(self, request, view, obj):
        if request.method is SAFE_METHODS:
            return True
        return obj.owner == request.user
    

class IsOwnerOrReadOnlyInList(BaseException):
    message = 'permission denied, you are not the owner'
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user

    def has_object_permission(self, request, view, obj):
        if request.method is SAFE_METHODS:
            return True
        return obj.board.owner == request.user
    

class IsOwnerOrReadOnlyInTask(BaseException):
    message = 'permission denied, you are not the owner'
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user

    def has_object_permission(self, request, view, obj):
        if request.method is SAFE_METHODS:
            return True
        return obj.user == request.user
    

class IsOwnerOrReadOnlyInLabel(BaseException):
    message = 'permission denied, you are not the owner'
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user

    def has_object_permission(self, request, view, obj):
        if request.mothed is SAFE_METHODS:
            return True
        return obj.board.owner == request.user
       