# encoding:utf-8
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from cmmedia.models import Image


class UserProfile(models.Model):
    """
    User profile 包含 用户介绍 ，头像，生日，地区等信息
    """
    user = models.OneToOneField(User)
    introduction = models.CharField(max_length=140,help_text=u'介绍')
    birthday = models.DateField(blank=True,null=True,help_text=u'生日')
    head_photo = models.OneToOneField(Image,related_name='head_photo',help_text=u'头像')
    region = models.CharField(max_length=50,help_text=u'地区')