"""
ASGI config for b_shop project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""
"""
ASGI config for b_shop project.
It exposes the ASGI callable as a module-level variable named ``application``.
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

# Import your routing patterns from the studio app
import studio.routing 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'b_shop.settings')

# The application object now routes between HTTP and WebSockets
application = ProtocolTypeRouter({
    # Handles standard HTTP requests (GET/POST)
    "http": get_asgi_application(),
    
    # Handles real-time WebSocket connections
    "websocket": AuthMiddlewareStack(
        URLRouter(
            studio.routing.websocket_urlpatterns
        )
    ),
})