""" Route for ChatConsumer
(is for the WebSockets for ASGI support of Django).
Routing to the URL ChatConsumer which 
will handle the chat functionality. """

from django.urls import path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    path("ws/chat/<room_name>/", ChatConsumer.as_asgi()),
]
