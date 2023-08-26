from uuid import UUID
from django.db.models import Q
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .models import User
from .serializers import (
    UserBriefSerializer,
    UserDetailSerializer,
)


class UserListAPIView(APIView):
    serializer_class = UserBriefSerializer

    def get(self, request: Request):
        users = (
            User.objects.filter(**request.query_params.dict()).all()
        )
        serializer = self.serializer_class(instance=users, many=True)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )
    
    def post(self, request: Request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer.save()
        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED,
        )
       