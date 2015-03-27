# encoding:utf-8
import logging
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from musiclist.models import Tag, MusicList
from musiclist.serializers import TagSerializers, MusicListSerializers

log = logging.getLogger('root')


class TagViewSet(ModelViewSet):
    """
    创建，获取，更新，删除一个Tag
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializers
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = u'pk'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class MusicListViewSet(ModelViewSet):
    """
    创建，获取，更新，删除一个歌单
    """
    queryset = MusicList.objects.all()
    serializer_class = MusicListSerializers
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = u'pk'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        musicl_list = super(MusicListViewSet,self).get_queryset()
        return musicl_list.filter(user=self.request.user)


