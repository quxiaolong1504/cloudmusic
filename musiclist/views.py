# encoding:utf-8
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from musiclist.models import Tag, MusicList
from musiclist.serializers import TagSerializers, MusicListSerializers


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