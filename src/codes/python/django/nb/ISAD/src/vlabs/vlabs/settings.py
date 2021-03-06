"""
Django settings for vlabs project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Django settings for the Software Engineering Virtual Lab (cse08)

SE_PATH = '/home/barun/codes/python/django/nb/ISAD/src/vlabs'
SECRET_KEY_PATH = '/'.join([SE_PATH, 'secret.txt',])
CREDENTIALS_PATH = '/'.join([SE_PATH, 'credentials.py',])

from utils import generate_secret_key as GS
from utils import generate_credentials as GC

# Create the secret key and credentials file at target locations
GS.generate_secret(SECRET_KEY_PATH)
GC.generate_credentials(SECRET_KEY_PATH, CREDENTIALS_PATH)


from credentials import *

# Make this unique, and don't share it with anybody.
SECRET_KEY = app_credentials['secret_key']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ADMINS = (
    ('Barun Saha', 'barun<DOT>saha04<AT>gmail<DOT>com'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': app_credentials['db_name'],
        'USER': app_credentials['db_user'],
        'PASSWORD': app_credentials['db_password'],
        'HOST': app_credentials['db_host'],
        'PORT': app_credentials['db_port'],
        'OPTIONS': {
            'init_command': 'SET storage_engine=INNODB'
        },
    }
}

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_js_reverse',
    'isad',
    'django_rq',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'vlabs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'vlabs.wsgi.application'


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = False
USE_L10N = True
USE_TZ = True

__ENV_PROD__ = True
#__ENV_PROD__ = False


# Enable this if you are hosting the lab behind reverse proxy
#REVERSE_PROXY_PREFIX = 'se'
# Enable this if no reverse proxy is used
REVERSE_PROXY_PREFIX = ''

if len(REVERSE_PROXY_PREFIX) > 0:
    REVERSE_PROXY_URL = '/' + REVERSE_PROXY_PREFIX
else:
    REVERSE_PROXY_URL = ''

JS_REVERSE_SCRIPT_PREFIX = REVERSE_PROXY_URL + '/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = REVERSE_PROXY_URL + '/isad_static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static_media/')

REDIS_QNAME = 'q_se'

RQ_QUEUES = {
    REDIS_QNAME: {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
        'PASSWORD': app_credentials['redis_password'],
        'DEFAULT_TIMEOUT': 120,
    }
}
