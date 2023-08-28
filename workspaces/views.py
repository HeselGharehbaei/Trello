import uuid

from django.shortcuts import get_object_or_404
from workspaces.models import Workspace, WorkspacesMembership
from workspaces.serializer import WorkspacesMembershipSerializer,WorkspaceSerializer, WorkspaceshortSerializer
from rest_framework import  status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from workspaces.permissions import IsWorkspaceAdminOrMemberReadOnly ,IsWorkspaceMember
from rest_framework import generics, mixins, status
from django.http import Http404
from django.db.models import Case, When

class workspaceDetail(APIView):
    serializer_class =  WorkspaceSerializer
    permission_classes = [IsWorkspaceAdminOrMemberReadOnly]

    def get(self, request, id):
        work = get_object_or_404(Workspace, id=id)
        self.check_object_permissions(self.request, work)

        serializer = WorkspaceSerializer(work, context={"request": request})
        return Response(serializer.data)

    def put(self, request, id):
        work = get_object_or_404(Workspace, id=id)
        self.check_object_permissions(self.request, work)

        serializer = WorkspaceSerializer(work, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        work = get_object_or_404(Workspace, id=id)
        self.check_object_permissions(self.request, work)

        work.delete()
        return Response(status=status.HTTP_200_OK)


class WorkspacesMemberDetail(APIView):
    serializer_class = WorkspacesMembershipSerializer
    permission_classes = [IsWorkspaceAdminOrMemberReadOnly]


    def get_object(self, id):
        obj = get_object_or_404(WorkspacesMembership, id=id)
        self.check_object_permissions(self.request, obj.workspace)

        return obj


    def delete(self, request, id):
        wmed = self.get_object(id)
        wmed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



    def put(self, request, id):
        wmed = self.get_object(id)
        serializer = WorkspacesMembershipSerializer(
            wmed, data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()

            
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkspacesMemberList(mixins.ListModelMixin,
                        generics.GenericAPIView,
                        mixins.CreateModelMixin):
    serializer_class = WorkspacesMembershipSerializer
    permission_classes = [IsWorkspaceAdminOrMemberReadOnly]

    def get_queryset(self):
        try:
            workspace = Workspace.objects.get(id=self.kwargs['id'])
            query_set = WorkspacesMembership.objects.filter(workspace=workspace)
        except:
            raise Http404
        return query_set


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



class WorkspaceList(mixins.ListModelMixin, mixins.CreateModelMixin,
                  generics.GenericAPIView):

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return WorkspaceshortSerializer 

        return WorkspaceshortSerializer

    def get_queryset(self):
        workspace_ids = WorkspaceshortSerializer.objects.filter(
            member=self.request.user).order_by('-access_level').values_list('workspace__id', flat=True)

        preserved = Case(*[When(id=id, then=pos)
                           for pos, id in enumerate(workspace_ids)])
        return Workspace.objects.filter(id__in=workspace_ids).order_by(preserved)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)