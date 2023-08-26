from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
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


class BoardListAPIView(APIView):
    serializer_class = BoardSerializer

    def get(self, request):
        boards = Board.objects.all()
        serializer = self.serializer_class(instance=boards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class BoardDetailAPIView(APIView):
    serializer_class = BoardSerializer
    
    def setup(self, request, id):
        try:
            self.Board = Board.objects.get(id=id)
        except Board.DoesNotExist:
            return Response(
                data={"detail": "Board Not Found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return super().setup(request, id)
        
    def get(self, request, id):
        serializer = self.serializer_class(
            instance=self.Board,
            context={"request": request},
        )
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )
    
    def put(self, request, id):
        serializer = self.serializer_class(
            instance=self.Board,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        self.Board.delete()
        return Response({"message": "board deleted"}, status=status.HTTP_200_OK)

        
class ListListAPIView(APIView):
    serializer_class = ListSerializer

    def get(self, request):
        list = List.objects.all()
        serializer = self.serializer_class(instance=list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ListDetailAPIView(APIView):
    serializer_class = ListSerializer

    def setup(self, request, id):
        try:
            self.List = List.objects.get(id=id)
        except List.DoesNotExist:
            return Response(
                data={"detail": "List Not Found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return super().setup(request, id)

    def get(self, request, id):
        serializer = self.serializer_class(
            instance=self.List,
            context={"request": request},
        )
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )
    
    def put(self, request, id):
        serializer = self.serializer_class(
            instance=self.List,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        self.List.delete()
        return Response({"message: list deleted"}, status=status.HTTP_200_OK) 


class TaskListAPIView(APIView):
    serializer_class = TaskSerializer

    def get(self, request):
        tasks = Task.objects.all()
        serializer = self.serializer_class(instance=tasks, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class TaskDetailAPIView(APIView):
    serializer_class = TaskSerializer

    def setup(self, request, id):
        try:
            self.Task = Task.objects.get(id=id)
        except Task.DoesNotExist:
            return Response(
                data={"detail": "Task Not Found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return super().setup(request, id)

    def get(self, request, id):
        serializer = self.serializer_class(
            instance=self.Task,
            context={"request": request},
        )
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )
    
    def put(self, request, id):
        serializer = self.serializer_class(
            instance=self.Task,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        self.Task.delete()
        return Response({"message: task deleted"}, status=status.HTTP_200_OK)


class CommentListView(APIView):
    serializer_class = CommentSerializer

    def get(self, request):
        comment = Comment.objects.all()
        serializer = self.serializer_class(instance=comment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class CommentDetailAPIView(APIView):
    serializer_class = CommentSerializer

    def setup(self, request, id):
        try:
            self.Comment = Comment.objects.get(id=id)
        except Comment.DoesNotExist:
            return Response(
                data={"detail": "Comment Not Found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return super().setup(request, id)
    
    def get(self, request, id):
        serializer = self.serializer_class(
            instance=self.Comment,
            context={"request": request},
        )
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )
    
    def put(self, request, pk):
        serializer = self.serializer_class(
            instance=self.Comment,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        self.Comment.delete()
        return Response({"message": "comment deleted"}, status=status.HTTP_200_OK)  


class LabelListAPIView(APIView):
    serializer_class = LabelSerializer

    def get(self, request):
        labels = Label.objects.all()
        serializer = self.serializer_class(instance=labels, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LabelDetailAPIView(APIView):
    serializer_class = LabelSerializer

    def setup(self, request, id):
        try:
            self.Label = Label.objects.get(id=id)
        except Label.DoesNotExist:
            return Response(
                data={"detail": "Label Not Found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return super().setup(request, id)

    def get(self, request, id):
        serializer = self.serializer_class(
            instance=self.Label,
            context={"request": request},
        )
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )
    
    def put(self, request, id):
        serializer = self.serializer_class(
            instance=self.Label,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        self.Label.delete()
        return Response({"message: label deleted"}, status=status.HTTP_200_OK) 