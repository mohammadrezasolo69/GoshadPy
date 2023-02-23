from core.settings.base import env

# Config CORS
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = ["DELETE", "GET", "OPTIONS", "PATCH", "POST", "PUT", ]

# Application definition

CSRF_TRUSTED_ORIGINS = env('CSRF_TRUSTED_ORIGINS').split(',')

