from django.urls import path
from workspaces.views import WorkspaceList, workspaceDetail, WorkspacesMemberList, WorkspacesMemberDetail

urlpatterns = [
    path('', WorkspaceList.as_view()),
    path('<int:pk>/', workspaceDetail.as_view()),
    path('<int:pk>/members/', WorkspacesMemberList.as_view()),
    path('members/<int:pk>/', WorkspacesMemberDetail.as_view()),

]