from base import *
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cloudmusic',
        'USER': 'root',
        'PASSWORD': 'qxlaylj',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS':{
            'init_command':'SET storage_engine=INNODB',
        },
    }
}