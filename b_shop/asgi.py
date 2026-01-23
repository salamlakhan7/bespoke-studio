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
import django # Add this import
from django.core.asgi import get_asgi_application

# 1. Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'b_shop.settings')

# 2. Initialize Django to populate the app registry
django.setup() 

# 3. Get the core ASGI application
django_asgi_app = get_asgi_application()

# 4. Import routing only AFTER django.setup()
import studio.routing
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            studio.routing.websocket_urlpatterns
        )
    ),
})
