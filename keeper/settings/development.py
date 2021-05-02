"""
Django settings for Keeper development.
"""
from keeper.settings.common import *
from keeper.settings.db import parse_db_url

SECRET_KEY = "django-insecure-=y&qw3+mu!aeh*p#+sbo403yv7ga1=_m)7zfuvdd(=@p%&8u4b"
DEBUG = True

ALLOWED_HOSTS = ["192.168.1.52", "localhost", "localhost.proxyman.io"]

os.environ.setdefault("DATABASE_URL", "postgres://127.0.0.1:5432/keeper")
db_url = os.environ["DATABASE_URL"]
DATABASES = {"default": parse_db_url(db_url)}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
}
