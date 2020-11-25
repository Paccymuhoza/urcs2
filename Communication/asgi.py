"""
ASGI entrypoint. Configures Django and then runs the application
defined in the ASGI_APPLICATION setting.
"""

import os
from channels.routing import get_channel_layer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Communication.settings")

channel_layer = get_channel_layer()