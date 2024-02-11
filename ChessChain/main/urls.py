from django.urls import path, include
from .views import index, RoomAPIView


urlpatterns = [
    path('', index),
    path('api/v1/room/', RoomAPIView.as_view()),
    path('api/v1/room/<int:pk>/', RoomAPIView.as_view())
]