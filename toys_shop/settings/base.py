"""
Django settings for toys_shop project.

Generated by 'django-admin startproject' using Django 5.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

# Imports
from pathlib import Path

import environ
from django.urls import reverse_lazy

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Environment
env = environ.Env()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY", default="fallback-key")

DEBUG = env.bool("DEBUG", default=False)

# Enable HTTP Strict Transport Security (HSTS)
# Forces the browser to always use HTTPS, even on next visits
SECURE_HSTS_SECONDS = 100500  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False

# Redirect all HTTP requests to HTTPS
# Ensures users never accidentally use an insecure connection
SECURE_SSL_REDIRECT = False

# Use secure cookies for user sessions
# Prevents session hijacking over unencrypted HTTP
SESSION_COOKIE_SECURE = False

# Use secure cookies for CSRF protection
# Prevents attackers from stealing CSRF tokens via sniffing
CSRF_COOKIE_SECURE = False

# Allow only trusted hosts (your production domain or IP)
# Replace with your actual domain
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

# User model
AUTH_USER_MODEL = "customers.User"

# Default login redirect URL
LOGIN_REDIRECT_URL = reverse_lazy("toys:index")

# DB
DATABASES = {}

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Storage
    "storages",
    # HTMX
    "django_htmx",
    # Toolbar
    "debug_toolbar",
    # Apllications
    "accounts",
    "customers",
    "orders",
    "toys",
    "carts",
    "wishlists",
    # django crispy forms
    "crispy_forms",
    "crispy_tailwind",
    #pinger
    "pinger.apps.PingerConfig"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "toys_shop.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # custom context processors
                "base.context_processors.cart_item_count",
                "base.context_processors.category_item_list",
                "base.context_processors.get_toy_search_form",
                "base.context_processors.wishlist_item_count",
            ],
        },
    },
]

WSGI_APPLICATION = "toys_shop.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa E501
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = "staticfiles/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# DROPBOX settings storage
STORAGES = {
    "default": {
        "BACKEND": "base.dropbox.PatchedDropboxStorage",
        "OPTIONS": {
            "oauth2_access_token": env("oauth2_access_token", default="dummy"),
            "oauth2_refresh_token": env("oauth2_refresh_token", default="dummy"),
            "app_key": env("app_key", default="dummy"),
            "app_secret": env("app_secret", default="dummy"),
            "root_path": "/media/",
        },
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Django debug tools
INTERNAL_IPS = ["127.0.0.1"]

# Email settings configuration

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="dummy")
EMAIL_PORT = env.int("EMAIL_PORT", default="dummy")
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default="dummy")
EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="dummy")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="dummy")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# TailWind crispy packs
CRISPY_ALLOWED_TEMPLATE_PACKS = ["tailwind"]
CRISPY_TEMPLATE_PACK = "tailwind"

# LOGS
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[{asctime}] {levelname} {name}: {message}",
            "style": "{",
        },
    },
    "handlers": {
        "ping_file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": BASE_DIR / "ping.log",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "pinger": {
            "handlers": ["ping_file"],
            "level": "INFO",
            "propagate": False,
        },
    },
}
