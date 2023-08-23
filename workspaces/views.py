import uuid

from django.shortcuts import get_object_or_404
from workspaces.models import Workspace, WorkspacesMembership
from workspaces.serializer import WorkspacesMembershipSerializer,WorkspaceSerializer, WorkspaceshortSerializer
from rest_framework import  status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User


class workspaceDetail(APIView):
    serializer_class =  WorkspaceSerializer

    def get(self, request, pk):
        work = get_object_or_404(Workspace, pk=pk)
        serializer = WorkspaceSerializer(work, context={"request": request})
        return Response(serializer.data)

    def put(self, request, pk):
        work = get_object_or_404(Workspace, pk=pk)
        serializer = WorkspaceSerializer(work, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        work = get_object_or_404(Workspace, pk=pk)
        work.delete()
        return Response(status=status.HTTP_200_OK)


class WorkspacesMemberDetail(APIView):
    serializer_class = WorkspacesMembershipSerializer
 

    def get_object(self, pk):
        obj = get_object_or_404(WorkspacesMembership, pk=pk)
        return obj





