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
    'cms',

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
    'wagtail.contrib.frontend_cache',

    'taggit',
    'grapple',
    'graphene_django',
    'channels',
    'corsheaders',
    'wagtail_headless_preview',

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


WAGTAIL_SITE_NAME = 'Wagtail Gatsby'

CORS_ORIGIN_ALLOW_ALL = True

GRAPHENE = {
    "SCHEMA": "grapple.schema.schema",
}
GRAPPLE_APPS = {
    "cms": ""
}

BASE_URL = 'http://localhost:8000'

HEADLESS_PREVIEW_CLIENT_URLS = {
    'default': 'http://localhost:8000/preview',
}

HEADLESS_PREVIEW_LIVE = True

# AWS


AWS_ACCESS_KEY_ID = env.str('AWS_ACCESS_KEY_ID', None)
AWS_SECRET_ACCESS_KEY = env.str('AWS_SECRET_ACCESS_KEY', None)

if AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY:
    AWS_S3_REGION_NAME = env.str('AWS_S3_REGION_NAME')
    AWS_S3_CUSTOM_DOMAIN = env.str('AWS_S3_CUSTOM_DOMAIN')
    AWS_STORAGE_BUCKET_NAME = env.str('AWS_STORAGE_BUCKET_NAME')

    AWS_IS_GZIPPED = True
    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_FILE_OVERWRITE = False
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    MEDIA_URL = AWS_S3_CUSTOM_DOMAIN + '/'
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'public, max-age=31536000',
    }

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


ASGI_APPLICATION = "asgi.channel_layer"
CHANNELS_WS_PROTOCOLS = ["graphql-ws"]
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgiref.inmemory.ChannelLayer",
        "ROUTING": "grapple.urls.channel_routing",
    }
}
