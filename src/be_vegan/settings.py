"""
Django settings for be_vegan project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from .config0 import SecretVariables

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SecretVariables.secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CORS_ORIGIN_ALLOW_ALL = True
ALLOWED_HOSTS = ["*"]
CSFR_TRUSTED_ORIGINS = ["*"]

AWS_ACCESS_KEY_ID = 'AKIA37SVVXBHZZZ2PQ2T'
AWS_SECRET_ACCESS_KEY = '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'
AWS_URL = 'https://cloud-cube-eu.s3.amazonaws.com/kgohyhjgpt5s'
AWS_S3_REGION_NAME = 'eu-west-1'
AWS_STORAGE_BUCKET_NAME = 'cloud-cube-eu'
AWS_DEFAULT_ACL = 'public-read'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'veggies.apps.VeggiesConfig',
    'storages',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  # <-- And here
    ],

}

ROOT_URLCONF = 'be_vegan.urls'

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

WSGI_APPLICATION = 'be_vegan.wsgi.application'

#DATABASE_ROUTERS = ['modules.mongodb_router.MongoDBRouter']

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
#

DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': SecretVariables.database_name,
#        'USER': SecretVariables.database_user,
#        'PASSWORD': SecretVariables.database_password,
#        'HOST': SecretVariables.database_host,
#        'PORT': '3306',
#                'OPTIONS': {
#                    'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
#                }
#    },
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'polska123',
        'HOST': 'db',
        'PORT': '5432',
    },
}

#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


AUTH_USER_MODEL="veggies.User"
# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# CORS_ORIGIN_WHITELIST =('*')
# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'pl'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


#PROJECT_ROOT = os.path.join(os.path.abspath(__file__))
#STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

#STATICFILES_DIRS = (
#	os.path.join(PROJECT_ROOT, 'static'),
#)

#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

#import dj_database_url
#prod_db = dj_database_url.config(conn_max_age=500, ssl_require = True)
#DATABASES['default'].update(prod_db)

#import django_heroku
#django_heroku.settings(locals())
