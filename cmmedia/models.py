# encoding=utf-8

from django.conf import settings
from django.db import models
from utils import choices

from utils.upload import UploadTo
# Create your models here.


class Image(models.Model):
    """
    cloud 图片资源
    """
    file = models.ImageField(upload_to='cmmedia')


class Artist(models.Model):
    """
    艺术家信息
    """
    name = models.CharField(max_length=50, help_text=u'姓名')
    head_photo = models.ImageField(upload_to='artists/head_photo/', blank=True, null=True, default=None)
    gender = models.CharField(max_length=10, choices=choices.GENDER)

    def __str__(self):
        return self.name

class Album(models.Model):
    """
    专辑信息
    """
    name = models.CharField(max_length=50, help_text=u'专辑名')
    thumbnail = models.ImageField(upload_to='albums/thumbail/', blank=True, null=True, )
    publishing_at = models.DateTimeField(auto_now_add=True, help_text=u'发行时间')

    def __str__(self):
        return self.name

class Music(models.Model):
    """
    cloud 音乐资源
    """
    name = models.CharField(max_length=50, help_text=u'歌名', default="")
    artists = models.ManyToManyField(Artist, related_name='musics', help_text=u'演唱者', default=None)
    album = models.ForeignKey(Album, related_name='musics', help_text=u'所属专辑', default=None)
    file = models.FileField(upload_to='musics', help_text=u'音乐文件', default=None)
    duration = models.CharField(max_length=30, help_text=u'歌曲时长', default="")

    def __str__(self):
        return self.name


