
from datetime import timedelta
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-b@u8504a4)67y@eu%+w4a$0c(svifwl+18old)b!4+&+uzv8f7'

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS=[]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
INSTALLED_APPS.extend(DJANGO_APPS)
THIRD_PARTY_APPS=[
    "rest_framework",
    "rest_framework.authtoken",
    'corsheaders',
    'whitenoise.runserver_nostatic',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'oauth2_provider',
    'tinymce',
    'drf_yasg',
    'djoser',

]
INSTALLED_APPS.extend(THIRD_PARTY_APPS)

MAIN_APPS=[
    'mainapps.accounts',
    'mainapps.bell_group',
    'mainapps.common',
    'mainapps.event',
    'mainapps.notification',
    'mainapps.user_profile',

]
INSTALLED_APPS.extend(MAIN_APPS)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'allauth.account.middleware.AccountMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,'templates'],
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

# WSGI_APPLICATION = 'core.wsgi.application'
WSGI_APPLICATION = 'core.wsgi.app'
AUTH_USER_MODEL='accounts.User'

# Database
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT'),
    }
}


# DATABASES['default']=dj_database_url.config()

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
AUTHENTICATION_BACKENDS = [
    "djoser.auth_backends.LoginFieldBackend",
]
DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': 'username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'USER_CREATE_PASSWORD_RETYPE':True,
    'PASSWORD_RESET_CONFIRM_RETYPE':True,
    'LOGOUT_ON_PASSWORD_CHANGE':True,
    'TOKEN_MODEL':None
}
DOMAIN=''
SITE_NAME='Sofire'
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'
STATIC_ROOT=BASE_DIR/ 'staticfiles_build' / 'static'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django_ses.SESBackend'
AWS_SES_REGION_NAME =  os.getenv("AWS_SES_REGION_NAME")
AWS_SES_REGION_ENDPOINT = f'email.{AWS_SES_REGION_NAME}.amazonaws.com'
AWS_SES_ACCESS_KEY_ID= os.getenv("AWS_SES_ACCESS_KEY_ID")
AWS_SES_SECRET_ACCESS_KEY= os.getenv("AWS_SES_SECRET_ACCESS_KEY")
USE_SES_V2 = True
AWS_SES_FROM_EMAIL= os.getenv("EMAIL_HOST_USER")
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 465  
# EMAIL_USE_SSL = True
# EMAIL_USE_TLS = False
EMAIL_HOST_USER = AWS_SES_FROM_EMAIL
DEFAULT_FROM_EMAIL=AWS_SES_FROM_EMAIL



SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=35),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=90),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,
    'ALGORITHM': 'HS256',
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,
    "TOKEN_OBTAIN_SERIALIZER": "mainapps.accounts.api.serializers.MyTokenObtainPairSerializer",

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}
AUTH_COOKIE='access'
AUTH_COOKIE_ACCESS_MAX_AGE=60*10
AUTH_COOKIE_REFRESH_MAX_AGE=60*60*24
AUTH_COOKIE_SECURE=False 
AUTH_COOKIE_HTTP_ONLY=True
AUTH_COOKIE_PATH='/'
AUTH_COOKIE_SAMESITE='None'
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'mainapps.accounts.authentication.AccountJWTAuthentication',
    )
}

CORS_ALLOW_ALL_ORIGINS=True
CORS_ORIGIN_ALLOW_ALL=True
# CORS_ALLOWED_ORIGINS = [
#     "https://simplybells.com",
# ]

CORS_ALLOW_CREDENTIALS=True
CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)



TINYMCE_DEFAULT_CONFIG = {
    'height': 360,
    'width': 800,
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'modern',
}
