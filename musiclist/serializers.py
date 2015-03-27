# encoding:utf-8
import sys,logging

from rest_framework import serializers
from musiclist.models import Tag, MusicList

log = logging.getLogger('root')

reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'quxl'


class TagSerializers(serializers.HyperlinkedModelSerializer):
    """
    标签 序列化器

    """

    class Meta:
        model = Tag
        fields = ('url','name',)


class MusicListSerializers(serializers.HyperlinkedModelSerializer):
    """
    歌单 序列化器
    """

    class Meta:
        model = MusicList
        fields = ('url', 'name', 'introduction', 'create_at', 'thumbnail','tags')


