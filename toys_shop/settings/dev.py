from .base import *

env.read_env(BASE_DIR / "toys_shop/.env")

# ALLOWED_HOSTS
ALLOWED_HOSTS = env("ALLOWED_HOSTS", default="").split(",")

RENDER_EXTERNAL_HOSTNAME = env("RENDER_EXTERNAL_HOSTNAME", default=None)
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# DB settings
DATABASES = {
    "default": env.db(
        "DATABASE_URL", default=f"sqlite:///{BASE_DIR / 'toys_db.sqlite3'}"
    )
}
