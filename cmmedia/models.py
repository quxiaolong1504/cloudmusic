# encoding=utf-8

from django.conf import settings
from django.db import models

from utils.upload import UploadTo
# Create your models here.


class Image(models.Model):
    """
    cloud 图片资源
    """
    file = models.ImageField(upload_to=UploadTo(upload_to=settings.MEDIA_USER_HEAD_PHOTO),max_length=1024*10)
