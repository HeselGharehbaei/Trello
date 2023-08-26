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
    
    
class UserLDetailAPIView(APIView):
    serializer_class = UserDetailSerializer

    def setup(self, request: Request, id: UUID):
        try:
            self.user= User.objects.get(id=id)
        except User.DoesNotExist:
            return Response(
                data={"detail": "User not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return super().setup(request, id)

    def get(self, request: Request, id: UUID):
        serializer = self.serializer_class(
            instance=self.user,
        )
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )

    def put(self, request: Request, id: UUID):
        serializer = self.serializer_class(
            instance=self.user,
            data=request.data,
        )
        if not serializer.is_valid():
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer.save()
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )

    def patch(self, request: Request, id: UUID):
        serializer = self.serializer_class(
            instance=self.user,
            data=request.data,
            partial=True,
        )
        if not serializer.is_valid():
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer.save()
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )

    def delete(self, request: Request, id: UUID):
        self.user.delete()
        return Response(
            data={"message": "User Deleted"},
            status=status.HTTP_200_OK,
        )
        