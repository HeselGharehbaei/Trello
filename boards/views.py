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
        serializer = self.serializer_class(data=request.POST)
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
        return Response({'message': 'board deleted'}, status=status.HTTP_200_OK)

        
class ListView(APIView):
    def get(self, request):
        list = List.objects.all()
        srz_list = ListSerializer(instance=list, many=True)
        return Response(srz_list.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        srz_list = ListSerializer(data=request.POST)
        if srz_list.is_valid():
            srz_list.save()
            return Response(srz_list.data, status=status.HTTP_201_CREATED)
        return Response(srz_list.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ListUpdateView(APIView):
    def put(self, request, pk):
        list = List.objects.get(pk=pk)
        srz_list = ListSerializer(instance=list, data=request.data, partial=True)
        if srz_list.is_valid():
            srz_list.save()
            return Response(srz_list.data, status=status.HTTP_200_OK)
        return Response(srz_list.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        list = List.objects.get(pk=pk)
        list.delete()
        return Response({"masage: list deleted"}, status=status.HTTP_200_OK) 


class CommentView(APIView):
    def get(self, request):
        comment = Comment.objects.all()
        srz_comment = CommentSerializer(instance=comment)
        return Response(srz_comment.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        srz_comment = CommentSerializer(data=request.POST)
        if srz_comment.is_valid():
            srz_comment.save()
            return Response(srz_comment.data, status=status.HTTP_200_OK)
        

class CommentUpdateView(APIView):
    def put(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        srz_comment = CommentSerializer(instance=comment, data=request.data, partial=True)
        if srz_comment.is_valid():
            srz_comment.save()
            return Response(srz_comment.data, status=status.HTTP_200_OK)
        return Response(srz_comment.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, reqest, pk):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response({"message": "Commetn deleted"}, status=status.HTTP_200_OK)  
