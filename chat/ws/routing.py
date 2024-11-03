from django.urls import path
from chat.ws import consumers

websocket_urlpatterns = [
    path('ws/chat/', consumers.ChatConsumer.as_asgi()),  # URL для WebSocket
]
