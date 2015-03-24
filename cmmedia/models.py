# encoding=utf-8

from django.conf import settings
from django.db import models

from utils.upload import UploadTo
# Create your models here.


class Image(models.Model):
    """
    cloud 图片资源
    """
    file = models.ImageField(max_length=1024*10,upload_to='cmmedia')
