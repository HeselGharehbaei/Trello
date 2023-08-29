from django.urls import path
from workspaces.views import WorkspaceList, WorkspaceDetail, WorkspacesMemberList, WorkspacesMemberDetail

urlpatterns = [
    path('', WorkspaceList.as_view()),
    path('<uuid:uuid>/', WorkspaceDetail.as_view()),
    path('<uuid:id>/members/', WorkspacesMemberList.as_view()),
    path('members/<uuid:id>/', WorkspacesMemberDetail.as_view()),

]