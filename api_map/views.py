# encoding:utf-8
from rest_framework.decorators import api_view
from rest_framework.response import Response

__author__ = 'quxl'

import logging
from django.utils.translation import ugettext_lazy as _
from rest_framework.reverse import reverse

log = logging.getLogger('root')

def api_root(request, format=None):
    return {
        _(u"accounts_url").strip(): reverse('accounts', request=request, format=format),
        _(u"resources_url").strip(): reverse('resources', request=request, format=format),
        }

@api_view(('GET',))
def get_api_root(request, format=None):
    return Response(api_root(request,format=format))
