# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cmmedia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('introduction', models.CharField(help_text='\u4ecb\u7ecd', max_length=140)),
                ('birthday', models.DateField(help_text='\u751f\u65e5', null=True, blank=True)),
                ('region', models.CharField(help_text='\u5730\u533a', max_length=50)),
                ('head_photo', models.OneToOneField(related_name='head_photo', to='cmmedia.Image', help_text='\u5934\u50cf')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
