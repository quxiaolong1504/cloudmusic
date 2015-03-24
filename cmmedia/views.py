# encoding=utf-8
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from cmmedia.models import Image
from cmmedia.serializers import ImageSerializer


class ImageViewSet(ModelViewSet):
    """
    创建和获取Image资源
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
