from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import(
    UserViewSet,
) 

router = SimpleRouter()
router.register("",  UserViewSet, basename="users")

app_name = "users"
urlpatterns = [
    path("", include(router.urls)),
]