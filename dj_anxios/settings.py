import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%11$h!nv-7!$f*ol92!9t5qullu20&8_c!)b))ds990vr(wzj1'
STRIPE_API_KEY_PUBLISHABLE = "pk_test_CNjmrHbvtgogUJImcLxhlK15"
STRIPE_API_KEY_HIDDEN = "sk_test_xNmM9WXHsxQZ8U3PGopqVeXg"

DEBUG = True

ALLOWED_HOSTS = []

# CART

SESSION_COOKIE_AGE = 86400
CART_SESSION_ID = 'cart'


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'apps.cart',
    'apps.core',
    'apps.order',
    'apps.store'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dj_anxios.urls'

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
                'apps.store.context_processors.menu_categories',
                'apps.cart.context_processors.cart'
            ],
        },
    },
]

WSGI_APPLICATION = 'dj_anxios.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = (
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator' },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator' },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator' },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator' },
)

# Internationalization
LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'GMT'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')