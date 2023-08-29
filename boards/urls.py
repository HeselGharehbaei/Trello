from django.urls import path
from .views import (
    BoardViewset,
    ListViewSet,
    TaskViewSet,
    CommentViewSet,
    LabelListViewSet,

)
from rest_framework import routers


app_name = 'boards'
urlpatterns = [

]


router = routers.SimpleRouter()
router.register('board', BoardViewset, basename='boards')
router.register('list', ListViewSet, basename='boards')
router.register('task', TaskViewSet, basename='boards')
router.register('comment', CommentViewSet, basename='boards')
router.register('lable', LabelListViewSet, basename='boards')
urlpatterns = router.urls