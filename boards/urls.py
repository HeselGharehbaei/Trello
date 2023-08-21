from django.urls import path
from .views import BoardListAPIView


urlpatterns = [
    path('', BoardListAPIView.as_view())
]
