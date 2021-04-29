import urllib.parse as urlparse

urlparse.uses_netloc.append("postgres")


def parse_db_url(url: str):
    url = urlparse.urlparse(url)
    path = url.path[1:]

    config = {}
    config.update(
        {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": urlparse.unquote(path or ""),
            "USER": urlparse.unquote(url.username or ""),
            "PASSWORD": urlparse.unquote(url.password or ""),
            "HOST": url.hostname or "",
            "PORT": url.port or "",
            "CONN_MAX_AGE": 0,
        }
    )

    return config
