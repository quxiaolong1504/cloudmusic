# encoding=utf-8
from rest_framework import serializers
from cmmedia.models import Image, Artist, Album, Music

__author__ = 'quxl'


class ImageSerializer(serializers.ModelSerializer):
    """
    Image 序列化器
    """
    class Meta:
        model = Image

class ArtistSerializer(serializers.ModelSerializer):
    """
    艺术家 序列化器
    """
    class Meta:
        model = Artist


class AlbumSerializer(serializers.ModelSerializer):
    """
    专辑 序列化器
    """
    class Meta:
        model = Album


class MusicSerializer(serializers.ModelSerializer):
    """
    音乐 序列化器
    """
    class Meta:
        model = Music
