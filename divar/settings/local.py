from .base import *

DEBUG = False
ALLOWED_HOSTS = ['']
MIDDLEWARE += [
    'silk.middleware.SilkyMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INSTALLED_APPS += [
    'silk',
    'debug_toolbar',
]
INTERNAL_IPS = [
    "127.0.0.1",
]
