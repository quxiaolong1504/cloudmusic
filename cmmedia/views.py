# encoding=utf-8
from django.utils.translation import ugettext_lazy as _
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from cmmedia.models import Image, Artist, Album, Music
from cmmedia.serializers import ImageSerializer, ArtistSerializer, AlbumSerializer, MusicSerializer


class ResourceURLView(APIView):
    allowed_methods = ['GET']

    def get(self,request,*args,**kwargs):
        return Response(self.get_url_dispach())
    def get_url_dispach(self,format=None):
         return {
        _(u"images_url").strip(): reverse('resource_image', request=self.request, format=format,),
        _(u"artists_url").strip(): reverse('artists-list', request=self.request, format=format),
        _(u"albums_url").strip(): reverse('albums-list', request=self.request, format=format),
        _(u"musics_url").strip(): reverse('musics-list', request=self.request, format=format),
        }


class ImageView(generics.CreateAPIView):
    """
    创建和获取Image资源
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ArtistViewSet(ModelViewSet):
    """
    创建，删除，更新，获取艺术家
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    lookup_field = u'pk'


class AlbumViewSet(ModelViewSet):
    """
    创建，删除，更新，获取专辑
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    lookup_field = u'pk'


class MusicViewSet(ModelViewSet):
    """
    创建，删除，更新，获取专辑
    """
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    lookup_field = u'pk'
