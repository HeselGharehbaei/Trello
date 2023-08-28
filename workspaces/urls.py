from django.urls import path
from workspaces.views import WorkspaceList, workspaceDetail, WorkspacesMemberList, WorkspacesMemberDetail

urlpatterns = [
    path('', WorkspaceList.as_view()),
    path('<uuid:id>/', workspaceDetail.as_view()),
    path('<uuid:id>/members/', WorkspacesMemberList.as_view()),
    path('members/<uuid:id>/', WorkspacesMemberDetail.as_view()),

]