"""
Title: Multi vendor eCommerce software application
Description: Multi-seller e-commerce platform.
Author: Hossain Chisty(Backend Developer)
Contact: hossain.chisty11@gmail.com
Github: https://github.com/hossainchisty
"""

import os
from pathlib import Path

import cloudinary
import cloudinary.api
import cloudinary.uploader
import sentry_sdk
from dotenv import load_dotenv
from sentry_sdk.integrations.django import DjangoIntegration

load_dotenv()  # take environment variables from .env.


BASE_DIR = Path(__file__).resolve().parent.parent

# cloudinary configration
cloudinary.config( 
  cloud_name = "ddotk1vza", 
  api_key = "974861548987528", 
  api_secret = "vI0azmX0-YDE0IGu9j-QJkb-5kk" 
)

SECRET_KEY = '52$5ujr925j_8)+c4+yhwik_+vq6e13#fxi5**_$rv80pn3(sf'


STRIPE_PUB_KEY = os.getenv('STRIPE_PUB_KEY')

STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')

sentry_sdk.init(
    dsn=os.getenv('DNS'),
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    # traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=False
)

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', os.getenv('PIP')]

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
]

LOCAL_APPS = [
    'core.apps.CoreConfig',
    'cart.apps.CartConfig',
    'order.apps.OrderConfig',
    'review.apps.ReviewConfig',
    'product.apps.ProductConfig',
    'vendor.apps.VendorConfig',
    'blog.apps.BlogConfig',
    'customers.apps.CustomersConfig',
    'wishlist.apps.WishlistConfig',
    'newsletter.apps.NewsletterConfig',
]

THIRD_PARTY_APPS = [
    'cloudinary',
    'django_countries',
    'crispy_forms',
    'crispy_tailwind',
    'taggit',
    'captcha',
    'debug_toolbar',
    'django_celery_results',
]

INSTALLED_APPS = DEFAULT_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'Project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'lomofy_cache',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
}

# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/1",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient"
#         },
#         "KEY_PREFIX": "example"
#     }
# }

# INTERNAL_IPS = [
#     '127.0.0.1',
# ]

SITE_ID = 1
WSGI_APPLICATION = 'Project.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom user model
AUTH_USER_MODEL = "customers.User"

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files configuration
STATIC_URL = '/static/'
CRISPY_TEMPLATE_PACK = "bootstrap4"
CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Mail configrations
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_SSL = os.getenv('EMAIL_USE_SSL')
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# Google reCAPTCHA
RECAPTCHA_PUBLIC_KEY = '6LfPy3QiAAAAAMyMyB2vyaE5Frgkk2bf5TRx0VJk'
RECAPTCHA_PRIVATE_KEY = '6LfPy3QiAAAAAGDzTWjU8gW25xCaJjXafgj_j6LM'

# Session configuration
CART_SESSION_ID = 'cart'
SESSION_COOKIE_AGE = 86400  # 24 hours in seconds
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# Celery Configurations
CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
# CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = os.getenv('TIME_ZONE')

LOGIN_URL = 'customer_sign_in'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = 'customer_sign_out'
LOGOUT_REDIRECT_URL = 'customer_sign_in'

# Security Principles
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_HSTS_SECONDS = 31536000
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# CSRF_COOKIE_SECURE = True

# Activate Django-Heroku.
if 'HEROKU' in os.environ:
    import django_heroku
    django_heroku.settings(locals())
