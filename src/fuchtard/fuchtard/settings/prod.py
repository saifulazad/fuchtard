from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    'maxisushi.kz',
    'www.maxisushi.kz',
    'mechanar.maxisushi.kz',
]

SPARKPOST_API_KEY = 'fc52712a253df3d28d69fdb10fd521271c36eb09'
FUCHTARD_ORDERS_EMAIL = 'order@maxisushi.kz'
FUCHTARD_NOREPLY_EMAIL = 'Maxi Sushi <noreply@maxisushi.kz>'

# LOGGING
LOGGING = {
    'version': 1,
    'handlers': {
        'mail_admins': {
            'class': 'main.utils.CustomAdminEmailHandler',
            'level': 'ERROR',
            # 'filters': ['special']
        }
    },
    'loggers': {
        'django': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            # 'propagate': True,
        },
    },
}