# encoding:utf-8
import logging

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from account.models import UserProfile
from account.serializers import UserSerializer, UserProfileSerializer


log = logging.getLogger('root')

class AccountURLView(APIView):
    allowed_methods = ['GET']

    def get(self,request,*args,**kwargs):
        return Response(self.get_url_dispach())
    def get_url_dispach(self,format=None):
         return {
        _(u"profile_url").strip(): reverse('accounts-profile', request=self.request, format=format),
        _(u"login_url").strip(): reverse('rest_framework:login', request=self.request, format=format),
        _(u"logout_url").strip(): reverse('rest_framework:logout', request=self.request, format=format),
        _(u"register_url").strip(): reverse('accounts-reg', request=self.request, format=format),
        }



class UserRegView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AccountsView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = None

    def get_object(self):
        return get_object_or_404(self.queryset,user=self.request.user)

