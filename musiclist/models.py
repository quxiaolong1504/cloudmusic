# encoding:utf-8
import logging
from django.contrib.auth.models import User

from django.db import models

log = logging.getLogger('root')


class Tag(models.Model):
    """
    标签 用户给音乐打标签 快速定位音乐
    """
    name = models.CharField(max_length=20, help_text=u'标签名称')
    user = models.ForeignKey(User, related_name='tags')

    def __str__(self):
        return self.name


class MusicList(models.Model):
    """
    歌单 信息模型
    """
    name = models.CharField(max_length=100, help_text=u'歌单名称', default="")
    user = models.ForeignKey(User, related_name='music_lists', help_text=u"歌单用者")
    create_at = models.DateTimeField(auto_now_add=True, help_text=u'创建时间')
    listen_count = models.IntegerField(default=0, help_text=u'收听数')
    tags = models.ManyToManyField(Tag, related_name='music_lists', help_text=u'标签列表',limit_choices_to={'pk__is':1} )
    introduction = models.CharField(max_length=200, help_text=u'歌单简介')
    thumbnail = models.ImageField(upload_to='musiclists/thumbnail',help_text=u'歌单缩略图',default=None)