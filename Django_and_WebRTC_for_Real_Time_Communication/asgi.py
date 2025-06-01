# Django_and_WebRTC_for_Real_Time_Communication/asgi.py
import os, django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing  # ← NE PAS importer le routing de la racine
from django.urls import path
from chat.consumers_graphql import GraphqlWsConsumer
from chat.consumers import SignalingConsumer
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django_and_WebRTC_for_Real_Time_Communication.settings")
django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
         URLRouter([
            path("graphql/", GraphqlWsConsumer.as_asgi()),
             path("ws/signaling/<str:room_code>/", SignalingConsumer.as_asgi()) 
        ])
    ),
})
