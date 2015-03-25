# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musiclist', '0002_auto_20150325_0737'),
    ]

    operations = [
        migrations.AddField(
            model_name='musiclist',
            name='thumbnail',
            field=models.ImageField(default=None, help_text='\u6b4c\u5355\u7f29\u7565\u56fe', upload_to=b'musiclists/thumbnail'),
            preserve_default=True,
        ),
    ]
