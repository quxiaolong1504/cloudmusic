# encoding=utf-8
from django.utils.translation import ugettext_lazy as _
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from cmmedia.models import Image
from cmmedia.serializers import ImageSerializer


class ResourceURLView(APIView):
    allowed_methods = ['GET']

    def get(self,request,*args,**kwargs):
        return Response(self.get_url_dispach())
    def get_url_dispach(self,format=None):
         return {
        _(u"images").strip(): reverse('resource_image', request=self.request, format=format,),
        }



class ImageView(generics.CreateAPIView):
    """
    创建和获取Image资源
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
