# encoding=utf-8
from rest_framework import serializers
from cmmedia.models import Image

__author__ = 'quxl'


class ImageSerializer(serializers.ModelSerializer):
    """
    Image 序列化器
    """
    class Meta:
        model = Image
        fields = ('file',)

