import openai
import firebase_admin
from pathlib import Path
from dotenv import load_dotenv
from os import getenv
from firebase_admin import credentials
from corsheaders.defaults import default_headers

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

APP_NAME = getenv('APP_NAME')

SECRET_KEY = getenv('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = [getenv('HOST_IP')]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'app.customer',
    'app.chatbot',
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

ROOT_URLCONF = 'apis.urls'

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

WSGI_APPLICATION = 'apis.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': getenv('DATABASE_NAME'),
#         'USER': getenv('DATABASE_USER'),
#         'PASSWORD': getenv('DATABASE_PASSWORD'),
#         'HOST': getenv('DATABASE_HOST'),
#         'PORT': getenv('DATABASE_PORT'),
#         'OPTIONS': {
#             'charset': 'utf8mb4',
#         },
#     }
# }

# Firebase
creds = credentials.Certificate(str(BASE_DIR / 'firebase_credentials.json'))
firebase_admin.initialize_app(creds)


# Password validation

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

# Rest API Framework Configurations

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'chatbot': '15/min',
    },
    'EXCEPTION_HANDLER': 'common.exception.exception_handler.ExceptionHandler'
}

# Jwt Config

JWT_ACCESS_SECRET = getenv('JWT_ACCESS_SECRET')
JWT_REFRESH_SECRET = getenv('JWT_REFRESH_SECRET')

# Encryption Key

SERVER_ENC_KEY = getenv('SERVER_ENC_KEY')

# OpenAI
openai.api_key = getenv('OPEN_AI_KEY')

# External Server

EXTERNAL_SERVER_HOST_URL = getenv('EXTERNAL_SERVER_HOST_URL')
EXTERNAL_SERVER_API_KEY = getenv('EXTERNAL_SERVER_API_KEY')

# Cors Configuration

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_HEADERS = (*default_headers, 'PROJECTID', 'APIKEY', 'CUSTOMERTOKEN')
CORS_ALLOW_CREDENTIALS = True

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'
STATICFILES_DIRS  = [BASE_DIR / 'static']

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
