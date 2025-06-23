"""
ASGI config for Channels project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import django
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter
import channelapp.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Channels.settings')
django.setup()

#application = get_asgi_application()
application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            channelapp.routing.websocket_urlpatterns
        )
    ),
})