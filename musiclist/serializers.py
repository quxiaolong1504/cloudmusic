# encoding:utf-8
from rest_framework import serializers
from musiclist.models import Tag, MusicList
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'quxl'


class TagSerializers(serializers.ModelSerializer):
    """
    标签 序列化器

    """

    class Meta:
        model = Tag
        fields = ('name',)


class MusicListSerializers(serializers.HyperlinkedModelSerializer):
    """
    歌单 序列化器
    """

    class Meta:
        model = MusicList
        fields = ('url', 'name', 'introduction', 'create_at', 'thumbnail','tags')


