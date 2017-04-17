"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

environment = os.environ.get("DJANGO_ENV", None)

if environment:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.%s" % os.environ["DJANGO_ENV"])
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.development")

application = get_wsgi_application()
