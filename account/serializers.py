# encoding:utf-8
import logging
from django.contrib.auth.models import User
from rest_framework import serializers
from account.models import UserProfile
from cmmedia.models import Image
from cmmedia.serializers import ImageSerializer

log = logging.getLogger('root')

__author__ = 'quxl'


class UserSerializer(serializers.ModelSerializer):
    """
    User register serizlizer
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], password=validated_data['password'])
        self.generate_profile(user)
        return user

    def generate_profile(self, user):
        profile = UserProfile(user=user)
        profile.save()


class UserProfileSerializer(serializers.ModelSerializer):
    head_photo = ImageSerializer()

    class Meta:
        model = UserProfile
        fields = ('first_name', 'introduction', 'gender', 'birthday', 'region', 'head_photo',)

    def update(self, instance, validated_data):
        """
        update user profile
        :param instance: the instance of UserProfile
        :param validated_data: the date , client update
        :return: UserProfile instance
        """
        hp = validated_data.pop('head_photo')
        profile = super(UserProfileSerializer, self).update(instance, validated_data)
        self.update_or_create_head_photo(profile, hp)
        return profile


    def update_or_create_head_photo(self, profile, hp):
        head_photo = profile.head_photo
        if not head_photo:
            head_photo = Image(file=hp['file'])
            head_photo.save()
            profile.head_photo = head_photo
            profile.save()
        else:
            head_photo.file = hp['file']
            head_photo.save()
        return profile

