# encoding:utf-8

from __future__ import unicode_literals
import logging

from django.core.urlresolvers import NoReverseMatch

from rest_framework.compat import OrderedDict
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.routers import DefaultRouter
from rest_framework.views import APIView

log = logging.getLogger('root')


class MyRouter(DefaultRouter):

     def __init__(self,api_map =None,*args,**kwargs):
        self.api_map = api_map
        super(MyRouter,self).__init__(*args,**kwargs)

     def get_api_root_view(self):

        """
        Return a view to use as the API root.
        """
        api_root_dict = OrderedDict()
        list_name = self.routes[0].name
        for prefix, viewset, basename in self.registry:
            api_root_dict[prefix] = list_name.format(basename=basename)
        api_map = self.api_map
        class APIRoot(APIView):
            """
            Cloud Music 内部文档
            =========
            如在使用中发现不便的地方，欢迎及时反馈。


            ## 团队成员
            Cloud Music由[GreenPine][2]创立

            欢迎[发邮件][1]给我

            [1]:mailto:quxl@snbway.com?subject=来自于Cloud_Music内部文档&body=首先在此表示感谢。您有什么想法和建议，可以直接email给我。GreenPine

            [2]:http://quxl.snbway.net



            """
            _ignore_model_permissions = True

            def __init__(self):
                self.api_map={}

            def get(self, request, *args, **kwargs):
                ret = OrderedDict()
                for key, url_name in api_root_dict.items():
                    try:
                        ret[key] = reverse(
                            url_name,
                            request=request,
                            format=kwargs.get('format', None)
                        )
                    except NoReverseMatch:
                        # Don't bail out if eg. no list routes exist, only detail routes.
                        continue
                if api_map:
                    diy_url=api_map(request)
                    for key in diy_url.keys():
                        ret[key]=diy_url[key]
                return Response(ret)

        return APIRoot.as_view()

