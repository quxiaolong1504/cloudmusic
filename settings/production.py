from base import *
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cloudmusic',
        'USER': 'quxl',
        'PASSWORD': 'quxl',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS':{
            'init_command':'SET storage_engine=INNODB',
        },
    }
}