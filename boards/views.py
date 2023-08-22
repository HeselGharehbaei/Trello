from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import BoardSerializer
from .models import Board
from rest_framework import status


class BoardListAPIView(APIView):
    serializer_class = BoardSerializer

    def get(self, Request):
        boards = Board.objects.all()
        serializer = self.serializer_class(instance=boards, many=True)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )
    
    # def post(self, Request):-------------------------------------------------------------------------------------------------------------------------------------------



class BoardsView(APIView):
    def get(self, request):
        boards = Board.objects.all()
        srz_boards = BoardSerializer(instance=boards, many=True)
        return Response(srz_boards.data, status=status.HTTP_200_OK)


class BoardCreateView(APIView):
    def post(self, request):
        pass





class BoardupdateView(APIView):
    def put(self, request):
        pass


class BoardDeleteView(APIView):
    def delete(self, request):
        pass



















