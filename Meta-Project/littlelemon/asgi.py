"""
ASGI config for littlelemon project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
=======
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
>>>>>>> e951807 (İlk proje yüklemesi)
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'littlelemon.settings')

application = get_asgi_application()
