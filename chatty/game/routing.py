from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('game/<str:game_name>/', consumers.GameConsumer.as_asgi()),
]