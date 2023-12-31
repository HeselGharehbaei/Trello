from rest_framework import viewsets
from rest_framework.views import APIView
from .models import User
from .serializers import (
    UserBriefSerializer,
    UserDetailSerializer,
    UserDashboardSerializer,
)
from .permissions import IsOwnerOrReadOnlyInUserDetail, IsOwnerOrReadOnlyInUserDashboard
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnlyInUserDetail]
    serializer_class = UserDetailSerializer
    lookup_field = "id"  

    def get_queryset(self):
        return User.objects.filter(**self.request.query_params.dict()).all()

    def get_serializer_class(self):
        if self.action in ['list']:
            return UserBriefSerializer
        return self.serializer_class 


class UserDashboardViewSet(viewsets.ViewSet):
    permission_classes = [IsOwnerOrReadOnlyInUserDashboard]
    queryset = User.objects.all() 

    def retrieve(self, request, pk):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer_class = UserDashboardSerializer(instance=user)
        return Response(data=serializer_class.data)
    