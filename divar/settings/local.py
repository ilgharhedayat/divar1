from .base import *

DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1"]
MIDDLEWARE += [
    "silk.middleware.SilkyMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

INSTALLED_APPS += [
    "silk",
    "debug_toolbar",
]
INTERNAL_IPS = [
    "127.0.0.1",
]
