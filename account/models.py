# encoding:utf-8
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from cmmedia.models import Image
from utils import choices


class UserProfile(models.Model):
    """
    User profile 包含 用户介绍 ，头像，生日，地区等信息
    """
    user = models.OneToOneField(User)
    gender = models.CharField(max_length=10,help_text=u'性别',
                              choices=choices.GENDER, default='',)
    first_name = models.CharField(max_length=20,help_text=u'昵称', default='')
    introduction = models.CharField(max_length=140,help_text=u'介绍')
    birthday = models.DateField(blank=True,null=True,help_text=u'生日')
    head_photo = models.OneToOneField(Image,related_name='head_photo',help_text=u'头像', null=True, blank=True)
    region = models.CharField(max_length=50,help_text=u'地区', null=True, blank=True)