from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-r&qhr2kj3qjz0sy-m8wc^o^wah6_m=td)hvjk%oex4s6yc$!(+'
DEBUG = False
ALLOWED_HOSTS = []
INSTALLED_APPS = [
    'app'
]
MIDDLEWARE = []
ROOT_URLCONF = 'build_upload.urls'
TEMPLATES = []
WSGI_APPLICATION = 'build_upload.wsgi.application'
DATABASES = {}
AUTH_PASSWORD_VALIDATORS = []
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LINODE_S3_BUCKET_DEV_DEPLOYMENTS = 'dev-deployments'
LINODE_S3_BUCKET_LIVE_DEPLOYMENTS = 'live-deployments'
LINODE_ENDPOINT_URL_DEV_DEPLOYMENTS = 'dev-deployments.eu-central-1.linodeobjects.com'
LINODE_ENDPOINT_URL_LIVE_DEPLOYMENTS = 'live-deployments.eu-central-1.linodeobjects.com'
