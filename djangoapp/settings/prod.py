from .base import *
import dj_database_url

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = ['mjcmauguiocarnon.fr', 'mjc-mauguio-carnon.com', 'www.mjc-mauguio-carnon.com', os.environ.get('HOST')]

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

AWS_S3_HOST = 's3-eu-west-1.amazonaws.com'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_LOCATION = 'static'
STATIC_ROOT="/"
STATIC_URL = "static/"
