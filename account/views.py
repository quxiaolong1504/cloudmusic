# encoding:utf-8
import logging
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from account.models import UserProfile

from account.serializers import UserSerializer, UserProfileSerializer

log = logging.getLogger('root')


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

