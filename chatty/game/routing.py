from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/<str:game_name>/', consumers.GameConsumer.as_asgi()),
]