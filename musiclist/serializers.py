# encoding:utf-8
from rest_framework import serializers
from musiclist.models import Tag, MusicList

__author__ = 'quxl'


class TagSerializers(serializers.ModelSerializer):
    """
    标签 序列化器

    """
    class Meta:
        model = Tag
        fields = ('name',)


class MusicListSerializers(serializers.ModelSerializer):
    """
    歌单 序列化器
    """

    class Meta:
        model = MusicList
        fields = ('name','introduction','create_at','tags')