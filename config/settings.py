from pathlib import Path

import environ
from django.urls import reverse_lazy

# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from the .env file
env = environ.Env()
env.read_env(BASE_DIR / ".env")

# Secret key for Django's security
SECRET_KEY = env.str("SECRET_KEY")

# Debug mode (False in production)
DEBUG = env.bool("DEBUG", False)

# List of allowed hostnames
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])

# List of Django's built-in apps
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# List of third-party apps (add here as needed)
THIRD_PARTY_APPS = [
    "simple_history",
    "crispy_forms",
    "crispy_tailwind",
]

# List of local apps (add your custom apps here)
LOCAL_APPS = [
    "apps.accounts",
    "apps.core",
]

# Development-only apps (enabled when DEBUG is True)
DEV_APPS = [
    "django_browser_reload",
]

# Combine all app lists into INSTALLED_APPS
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
if DEBUG:
    INSTALLED_APPS.extend(DEV_APPS)

# Middleware settings
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
]

# If app is in DEBUG Mode, load DEV Middlewares
if DEBUG:
    MIDDLEWARE.extend([
        "django_browser_reload.middleware.BrowserReloadMiddleware",
    ])

# Root URL configuration
ROOT_URLCONF = "config.urls"

# Template settings
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
                "apps.core.context_processors.website_name"
            ],
        },
    },
]

# WSGI application
WSGI_APPLICATION = "config.wsgi.application"

# Database configuration (SQLite in this example)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation settings
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME":
            "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Language and timezone settings
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = False
USE_L10N = True
USE_TZ = False

# Static file settings
STATIC_URL = "static/"
STATIC_ROOT = "static/dist"
STATICFILES_DIRS = ["static/src"]

# Locale paths for translations (if needed)
LOCALE_PATHS = ["apps.locale"]

# Default auto field for database models
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Duration of a session cookie's validity in seconds
SESSION_COOKIE_AGE = 86400

# Controls whether the session expires when the browser is closed
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Define the storage backend for managing static files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Define the allowed template packs for django-crispy-forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"

# Set the default template pack for django-crispy-forms to Tailwind CSS
CRISPY_TEMPLATE_PACK = "tailwind"

# Set Custom User model as Auth User
AUTH_USER_MODEL = "accounts.CustomUser"

# Redirect to the login page when authentication is required.
LOGIN_URL = reverse_lazy("accounts:login")

# Redirect users to the previous page after login (empty for default behavior).
LOGIN_REDIRECT_URL = reverse_lazy("core:index")

# Redirect to the login page after logging out.
LOGOUT_REDIRECT_URL = reverse_lazy("accounts:login")

# Website Name. This is used in templates.
WEBSITE_NAME = "Django Templates"
