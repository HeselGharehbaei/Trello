from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
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
from rest_framework import status


class BoardsView(APIView):
    def get(self, request):
        boards = Board.objects.all()
        srz_boards = BoardSerializer(instance=boards, many=True)
        return Response(srz_boards.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        srz_board = BoardSerializer(data=request.POST)
        if srz_board.is_valid():
            srz_board.save()  
            return Response(srz_board.data, status=status.HTTP_201_CREATED)
        return Response(srz_board.errors, status=status.HTTP_400_BAD_REQUEST)  


class BoardUpdateView(APIView):
    def put(self, request, id):
        board = Board.objects.get(pk=id)
        srz_board =  BoardSerializer(instance=board, data=request.data, partial=True)
        if srz_board.is_valid():
            srz_board.save()
            return Response(srz_board.data, status=status.HTTP_200_OK)
        return Response(srz_board.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        board = Board.objects.get(pk=id)
        board.delete()
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
