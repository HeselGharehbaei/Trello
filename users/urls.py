from django.urls import path
from .views import(
    UserListAPIView,
    UserLDetailAPIView,
) 

app_name = "users"
urlpatterns = [
    path('', UserListAPIView.as_view(), name= "user_list"),
    path('<uuid:id>/', UserLDetailAPIView.as_view(), name= "user_details"),
]