from django.conf import settings
from pathlib import Path
import os

DEBUG = True
ALLOWED_HOSTS = ['*']
settings.INSTALLED_APPS += [
    'core',
    'silk',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'simple_lms',
        'USER': 'simple_user',
        'PASSWORD': 'simple_password',
        'HOST': 'simpledb',
    }
}

BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'