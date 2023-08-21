from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import BoardSerializer
from .models import Board


class BoardListAPIView(APIView):
    serializer_class = BoardSerializer

    def get(self, Request):
        boards = Board.objects.all()
        serializer = self.serializer_class(instance=boards, many=True)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )
    
    # def post(self, Request):
