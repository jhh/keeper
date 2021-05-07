"""
Django settings for Puka production deployments.
"""
from django.core.management.utils import get_random_secret_key
from keeper.settings.common import *
from keeper.settings.db import parse_db_url

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", default=get_random_secret_key())
DEBUG = False

ALLOWED_HOSTS = ["*"]

db_url = os.getenv("DATABASE_URL", default="")
DATABASES = {"default": parse_db_url(db_url)}

# DATABASES = {"default": dj_database_url.config(conn_max_age=600, ssl_require=True)}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": (
                "%(asctime)s [%(process)d] [%(levelname)s] "
                + "pathname=%(pathname)s lineno=%(lineno)s "
                + "funcname=%(funcName)s %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "null": {
            "level": "DEBUG",
            "class": "logging.NullHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "testlogger": {
            "handlers": ["console"],
            "level": "INFO",
        }
    },
}

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
