from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import (
    UserBriefSerializer,
    UserDetailSerializer,
)
from .permissions import IsOwnerOrReadOnlyInUserDetail


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnlyInUserDetail]
    serializer_class = UserDetailSerializer
    lookup_field = "id"  

    def get_queryset(self):
        return User.objects.filter(**self.request.query_params.dict()).all()

    def get_serializer_class(self):
        if self.action in ['list']:
            return UserBriefSerializer
        return self.serializer_class 
    