import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from django.core.asgi import get_asgi_application

import game.routing
# import wstest.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatty.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            game.routing.websocket_urlpatterns,
            # wstest.routing.websocket_urlpatterns,
        )
    )
})
