# studio/routing.py
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    # Changed .as_async() to .as_asgi()
    re_path(r'ws/chat/(?P<room_id>\d+)/$', consumers.ChatConsumer.as_asgi()),
]