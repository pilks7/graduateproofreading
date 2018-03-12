"""
WSGI config for grad project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


#added from blog, no idea what this does...
import signal

import sys
import traceback

import time
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise



application = DjangoWhiteNoise(application)
#end


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "grad.settings")

application = get_wsgi_application()
