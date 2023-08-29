from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import(
    UserViewSet,
    UserDashboardViewSet,
) 

user_router = SimpleRouter()
user_dashboard_router = SimpleRouter()
user_router.register("",  UserViewSet, basename="users")
user_dashboard_router.register("",  UserDashboardViewSet, basename="dashboard")

app_name = "users"
urlpatterns = [
    path("", include(user_router.urls)),
    path("", include(user_dashboard_router.urls)),
]
