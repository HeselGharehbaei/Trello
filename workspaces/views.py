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
