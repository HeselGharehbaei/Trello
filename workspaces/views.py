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


class workspaceDetail(APIView):
    serializer_class =  WorkspaceSerializer
    permission_classes = [IsWorkspaceAdminOrMemberReadOnly]

    def get(self, request, pk):
        work = get_object_or_404(Workspace, pk=pk)
        self.check_object_permissions(self.request, work)

        serializer = WorkspaceSerializer(work, context={"request": request})
        return Response(serializer.data)

    def put(self, request, pk):
        work = get_object_or_404(Workspace, pk=pk)
        self.check_object_permissions(self.request, work)

        serializer = WorkspaceSerializer(work, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        work = get_object_or_404(Workspace, pk=pk)
        self.check_object_permissions(self.request, work)

        work.delete()
        return Response(status=status.HTTP_200_OK)


class WorkspacesMemberDetail(APIView):
    serializer_class = WorkspacesMembershipSerializer
    permission_classes = [IsWorkspaceAdminOrMemberReadOnly]


    def get_object(self, pk):
        obj = get_object_or_404(WorkspacesMembership, pk=pk)
        self.check_object_permissions(self.request, obj.workspace)

        return obj


    def delete(self, request, pk):
        wmed = self.get_object(pk)
        wmed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



    def put(self, request, pk):
        wmed = self.get_object(pk)
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
            workspace = Workspace.objects.get(pk=self.kwargs['pk'])
            query_set = WorkspacesMembership.objects.filter(workspace=workspace)
        except:
            raise Http404
        return query_set

