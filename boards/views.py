from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .permissions import (
    IsOwnerOrReadOnlyInBoard,
    IsOwnerOrReadOnlyInList,
    IsOwnerOrReadOnlyInLabel,
    IsOwnerOrReadOnlyInTask,
    IsMemberBoardOrnot,
    IsMemberOfTheTask,
)
from .serializers import (
    BoardSerializer,
    ListSerializer,
    TaskSerializer,
    CommentSerializer,
    LabelSerializer,
)
from .models import (
    Board,
    List,
    Task,
    Comment,
    Label,
)


class BoardViewset(viewsets.ViewSet):
    permission_classes = [IsOwnerOrReadOnlyInBoard, IsMemberBoardOrnot]
    serializer_class = BoardSerializer

    def Board(self, request, id):
        return Board.objects.get(pk=id)
    
    def list(self, request):
        boards = Board.objects.all()
        serializer = self.serializer_class(instance=boards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    def retrieve(self, request, id):
        serializer = self.serializer_class(
            instance=self.Board,
            context={"request": request},
        )
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )
    
    def update(self, request, id):
        serializer = self.serializer_class(
            instance=self.Board,
            data=request.data,
            partial=True,
        )
        self.check_object_permissions(request=request, obj=self.Board)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, id):
        self.check_object_permissions(request=request, obj=self.Board)
        self.Board.delete()
        return Response({"message": "board deleted"}, status=status.HTTP_200_OK)

        
class ListViewSet(viewsets.ViewSet):
    permission_classes = [IsOwnerOrReadOnlyInList]
    serializer_class = ListSerializer
    
    def List(self, request, id):
        return List.objects.get(pk=id)

    def list(self, request):
        list = List.objects.all()
        serializer = self.serializer_class(instance=list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, id):
        serializer = self.serializer_class(
            instance=self.List,
            context={"request": request},
        )
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )
    
    def update(self, request, id):
        serializer = self.serializer_class(
            instance=self.List,
            data=request.data,
            partial=True,
        )
        self.check_object_permissions(request=request, obj=self.List)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, id):
        self.check_object_permissions(request=request, obj=self.List)
        self.List.delete()
        return Response({"message: list deleted"}, status=status.HTTP_200_OK) 


class TaskViewSet(viewsets.ViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnlyInTask]
    
    def Task(self, request, id):
        return Task.objects.get(pk=id)
    
    def list(self, request):
        tasks = Task.objects.all()
        serializer = self.serializer_class(instance=tasks, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, id):
        serializer = self.serializer_class(
            instance=self.Task,
            context={"request": request},
        )
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )
    
    def update(self, request, id):
        serializer = self.serializer_class(
            instance=self.Task,
            data=request.data,
            partial=True,
        )
        self.check_object_permissions(request=request, obj=self.Task)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destory(self, request, id):
        self.check_object_permissions(request=request, obj=self.Task)
        self.Task.delete()
        return Response({"message: task deleted"}, status=status.HTTP_200_OK)


class CommentViewSet(viewsets.ViewSet):
    serializer_class = CommentSerializer
    permission_classes = []

    def Commetn(self, request, id):
        return Comment.objects.get(pk=id)

    def list(self, request):
        comment = Comment.objects.all()
        serializer = self.serializer_class(instance=comment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, id):
        serializer = self.serializer_class(
            instance=self.Commetn,
            context={"request": request},
        )
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )
    
    def update(self, request, pk):
        serializer = self.serializer_class(
            instance=self.Commetn,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destory(self, request, id):
        self.check_object_permissions(request=request, obj=self.Commetn)
        self.Commetn.delete()
        return Response({"message": "comment deleted"}, status=status.HTTP_200_OK)  


class LabelListViewSet(viewsets.ViewSet):
    permission_classes = [IsOwnerOrReadOnlyInLabel]
    serializer_class = LabelSerializer
    
    def Label(self, request, id):
        return Label.objects.get(pk=id)

    def list(self, request):
        labels = Label.objects.all()
        serializer = self.serializer_class(instance=labels, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, id):
        serializer = self.serializer_class(
            instance=self.Label,
            context={"request": request},
        )
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )
    
    def update(self, request, id):
        serializer = self.serializer_class(
            instance=self.Label,
            data=request.data,
            partial=True,
        )
        self.check_object_permissions(request=request, obj=self.Label)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        self.check_object_permissions(request=request, obj=self.Label)
        self.Label.delete()
        return Response({"message: label deleted"}, status=status.HTTP_200_OK)
     