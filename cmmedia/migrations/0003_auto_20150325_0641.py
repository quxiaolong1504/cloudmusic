# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmmedia', '0002_auto_20150325_0628'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music',
            old_name='albums',
            new_name='album',
        ),
        migrations.AlterField(
            model_name='artist',
            name='head_photo',
            field=models.ImageField(default=None, null=True, upload_to=b'artists/head_photo/', blank=True),
            preserve_default=True,
        ),
    ]
