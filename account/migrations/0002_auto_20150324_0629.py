# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='head_photo',
            field=models.OneToOneField(related_name='head_photo', null=True, blank=True, to='cmmedia.Image', help_text='\u5934\u50cf'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='region',
            field=models.CharField(help_text='\u5730\u533a', max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
    ]
