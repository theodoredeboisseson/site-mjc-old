import os

import dj_database_url
from dotenv import load_dotenv

from .base import *

# load env variables
load_dotenv()

SECRET_KEY = 'luf*lin!+xg$hf2z-m*c9b)kaamk3xm$+xf@5@dxc3tw!t31mt'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
