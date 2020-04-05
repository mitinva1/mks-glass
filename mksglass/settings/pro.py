from .base import *
DEBUG = False
ADMINS = (
    ('mitinva1', 'mitinva1@gmail.com'),
)
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mitinva1db1',
        'USER': 'mitinva1',
        'PASSWORD': 'runs27089',
    }
}