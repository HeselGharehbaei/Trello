from rest_framework import permissions
from workspaces.models import WorkspacesMembership


class IsWorkspaceAdminOrMemberReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        try: 
            wome = WorkspacesMembership.objects.get(member=request.user, workspace=obj)
        except WorkspacesMembership.DoesNotExist:
            return False
        
        if request.method in permissions.SAFE_METHODS:
            return True
        return wome.access_level == 2


class IsWorkspaceMember(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            wome = WorkspacesMembership.objects.get(member=request.user, workspace=obj)
        except WorkspacesMembership.DoesNotExist:
            return False
        return True
