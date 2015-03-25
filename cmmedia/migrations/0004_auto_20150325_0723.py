# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmmedia', '0003_auto_20150325_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='file',
            field=models.FileField(default=None, help_text='\u97f3\u4e50\u6587\u4ef6', upload_to=b'musics'),
            preserve_default=True,
        ),
    ]
