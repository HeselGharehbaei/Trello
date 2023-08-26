from django.urls import path
from .views import (
    BoardListAPIView,
    BoardDetailAPIView,
    ListListAPIView,
    ListDetailAPIView,
    TaskListAPIView,
    TaskDetailAPIView,
    CommentListView,
    CommentDetailAPIView,
    LabelListAPIView,
    LabelDetailAPIView,
)

app_name = 'board'
urlpatterns = [
    path('', BoardListAPIView.as_view(), name='board'),
    path('update/<uuid:id>/', BoardDetailAPIView.as_view(), name='board_update'),
    path('list/', ListListAPIView.as_view(), name='list'),
    path('list/update/<uuid:id>/', ListDetailAPIView.as_view(), name='list_update'),
    path('task/', TaskListAPIView.as_view(), name='task'),
    path('task/update/<uuid:id>/', TaskDetailAPIView.as_view(), name='task_update'),
    path('comment/', CommentListView.as_view(), name='comment'),
    path('comment/update/<uuid:id>', CommentDetailAPIView.as_view(), name='comment_update'),
    path('label/', LabelListAPIView.as_view(), name='label'),
    path('label/update/<uuid:id>', LabelDetailAPIView.as_view(), name='label_update'),
]
