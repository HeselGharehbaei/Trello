from django.urls import path
from .views import (
    BoardsView,
    BoardUpdateView,
    ListView,
    ListUpdateView,
    CommentView,
    CommentUpdateView,
)

app_name = 'board'
urlpatterns = [
    path('', BoardsView.as_view(), name='board'),
    path('update/<uuid:id>/', BoardUpdateView.as_view(), name='board_update'),
    path('list/', ListView.as_view(), name='list'),
    path('list/update/<uuid:pk>/', ListUpdateView.as_view(), name='list_update'),
    path('commetn/', CommentView.as_view(), name='commetn'),
    path('comment/update/<uuid:pk>', CommentUpdateView.as_view(), name='commetn_update')

]
