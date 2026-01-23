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

# This must come BEFORE importing studio.routing or consumers
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'b_shop.settings')

application = get_asgi_application()

# Import your routing only AFTER calling get_asgi_application()
import studio.routing
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    "http": application,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            studio.routing.websocket_urlpatterns
        )
    ),
})
