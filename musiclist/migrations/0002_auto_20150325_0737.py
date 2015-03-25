# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musiclist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='musiclist',
            old_name='master',
            new_name='user',
        ),
    ]
