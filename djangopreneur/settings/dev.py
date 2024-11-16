from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Configuration of Django-vite
DJANGO_VITE = {
    "default": {"dev_mode": True},
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-c^-6%$lk7+6hoz1a0fms&6ue+))i(^6fnb)y68=1#vy#3*&%4("

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

try:
    from .local import *
except ImportError:
    pass
