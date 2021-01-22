from .base import *

import dj_database_url
import django_heroku
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com']


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
DATABASES = {
    'default': db_from_env
}

django_heroku.settings(locals())