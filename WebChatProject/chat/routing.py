""" Route for ChatConsumer
(is for the WebSockets for ASGI support of Django).
Routing to the URL ChatConsumer which 
will handle the chat functionality. """

from django.urls import path, include
from .consumers import ChatConsumer

websocket_urlpatterns = [
    path("", ChatConsumer.as_asgi()),
]
