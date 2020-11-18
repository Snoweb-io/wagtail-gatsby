import os
import environ

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
env = environ.Env()
environ.Env.read_env(BASE_DIR + '/.env')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]

INSTALLED_APPS = [
    'cms.apps.CmsConfig',

    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'wagtail.contrib.settings',

    'taggit',
    'grapple',
    'graphene_django',
    'corsheaders',
    'django_celery_results',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    "django.contrib.sitemaps",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

DEBUG = True
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')
MEDIA_URL = '/media/'
ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'
SITE_ID = 1
SECRET_KEY = '[V$xMycv[(YwVThQD+p[s@Wb@Ygy@:`M%D3I8Fs2tJ^Aw#ac$AJ65".*]uwPaK_'

# End of Django Settings


WAGTAIL_SITE_NAME = env.str('WAGTAIL_SITE_NAME', 'Wagtail Gatsby')

CORS_ORIGIN_ALLOW_ALL = True

GRAPHENE = {
    "SCHEMA": "grapple.schema.schema",
}
GRAPPLE_APPS = {
    "cms": ""
}

BASE_URL = 'http://localhost:8000'

HEADLESS_PREVIEW_CLIENT_URLS = {
    'localhost': 'http://localhost:8000',
}

HEADLESS_PREVIEW_LIVE = True

# AWS


AWS_ACCESS_KEY_ID = env.str('AWS_ACCESS_KEY_ID', None)
AWS_SECRET_ACCESS_KEY = env.str('AWS_SECRET_ACCESS_KEY', None)
AWS_S3_REGION_NAME = env.str('AWS_S3_REGION_NAME')
AWS_S3_CUSTOM_DOMAIN = env.str('AWS_S3_CUSTOM_DOMAIN')
AWS_STORAGE_BUCKET_NAME = env.str('AWS_STORAGE_BUCKET_NAME')
AWS_DISTRIBUTION_ID = env.str('AWS_DISTRIBUTION_ID')

AWS_IS_GZIPPED = True
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_FILE_OVERWRITE = False
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'public, max-age=31536000',
}

if AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY:
    MEDIA_URL = AWS_S3_CUSTOM_DOMAIN + '/'


# LOGGING

DJANGO_LOG_LEVEL = env.str('DJANGO_LOG_LEVEL', 'DEBUG')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'cms': {
            'handlers': ['console'],
            'level': DJANGO_LOG_LEVEL,
        },
    },
}

# CELERY

CMS_BROKER_URL = env.str('CMS_BROKER_URL', 'redis://localhost:6379/0')
CMS_RESULT_BACKEND = 'django-db'
CMS_CACHE_BACKEND = 'django-cache'
CMS_TIMEZONE = env.str('CMS_TIMEZONE', 'Europe/Paris')
CMS_TASK_TRACK_STARTED = True
CMS_TASK_TIME_LIMIT = 12 * 60 * 60
