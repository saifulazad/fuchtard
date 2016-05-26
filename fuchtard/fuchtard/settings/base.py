"""
Django settings for fuchtard project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9t!sc1+#0zh@%c+xyiq&dlg_ri-_*7jfl!tg!lt#c0+1s9e6%p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'django.contrib.humanize',
    'django_extensions',
    'debug_toolbar',
    'webpack_loader',
    'widget_tweaks',
    'main',
    'food',
    'order',
    'panel',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fuchtard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        # 'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
            # 'loaders': [
            #     ('django.template.loaders.cached.Loader', [
            #         'django.template.loaders.filesystem.Loader',
            #         'django.template.loaders.app_directories.Loader',
            #     ]),
            # ],
        },
    },
]

WSGI_APPLICATION = 'fuchtard.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fuchtard',
        'USER': 'fuchtard',
        'PASSWORD': 'fuchtard',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = (
    'social.backends.vk.VKOAuth2',
    # 'social.backends.mailru.MailruOAuth2',
    # 'social.backends.odnoklassniki.OdnoklassnikiOAuth2',
    # 'social.backends.twitter.TwitterOAuth',
    # 'social.backends.facebook.Facebook2OAuth2',
    # 'social.backends.google.GoogleOpenId',
    # 'social.backends.google.GoogleOAuth2',
    # 'social.backends.google.GoogleOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Almaty'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '..', '..', 'static_content', 'static', )
STATICFILES_DIRS = [
    ('components', os.path.join(BASE_DIR, '..', '..', 'bower_components', ), ),
    ('webpack_bundles', os.path.join(BASE_DIR, '..', '..', 'webpack_bundles')),
    # We do this so that django's collectstatic copies or our bundles to the
    # STATIC_ROOT or syncs them to whatever storage we use.

]

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'webpack_bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, '..', '..', 'webpack-stats.json'),
    },
}


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', '..', 'static_content', 'media', )


# EMAIL
EMAIL_BACKEND = 'sparkpost.django.email_backend.SparkPostEmailBackend'
