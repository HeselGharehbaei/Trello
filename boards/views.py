from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import BoardSerializer
from .serializers import ListSerializer
from .serializers import TaskSerializer
from .serializers import CommentSerializer
from .serializers import LabelSerializer
from .models import Board
from .models import List
from .models import Task
from .models import Comment
from .models import Label
from rest_framework import status


class BoardListAPIView(APIView):
    serializer_class = BoardSerializer

    def get(self, Request):
        boards = Board.objects.all()
        serializer = self.serializer_class(instance=boards, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    # def post(self, Request):-------------------------------------------------------------------------------------------------------------------------------------------



class BoardsView(APIView):
    def get(self, request):
        boards = Board.objects.all()
        srz_boards = BoardSerializer(instance=boards, many=True)
        return Response(srz_boards.data, status=status.HTTP_200_OK)


class BoardCreateView(APIView):
    def post(self, request):
        srz_board = BoardSerializer(data=request.POST)
        if srz_board.is_valid():
            srz_board.save()  
            return Response(srz_board.data, status=status.HTTP_201_CREATED)
        return Response(srz_board.errors, status=status.HTTP_400_BAD_REQUEST)  


class BoardupdateView(APIView):
    def put(self, request, pk):
        board = Board.objects.get(pk=pk)
        srz_board =  BoardSerializer(instance=board, data=request.data, partial=True)
        if srz_board.is_valid():
            srz_board.save()
            return Response(srz_board.data, status=status.HTTP_200_OK)
        return Response(srz_board.errors, status=status.HTTP_400_BAD_REQUEST)


class BoardDeleteView(APIView):
    def delete(self, request, pk):
        board = Board.objects.get(pk=pk)
        board.delete()
        return Response({'message': 'board deleted'}, status=status.HTTP_200_OK)

        
class ListView(APIView):
    def get(self, request):
        list = List.objects.all()
        srz_list = ListSerializer(instance=list, many=True)
        return Response(srz_list.data, status=status.HTTP_200_OK)
    

class ListCreatView(APIView):
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
    

class ListDeleteView(APIView):
    def delete(self, request, pk):
        list = List.objects.get(pk=pk)
        list.delete()
        return Response({"masage: list deleted"}, status=status.HTTP_200_OK) 



















