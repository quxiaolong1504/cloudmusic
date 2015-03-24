# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_userprofile_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(default=b'', help_text='\u6027\u522b', max_length=10, choices=[(b'male', b'male'), (b'female', b'female')]),
            preserve_default=True,
        ),
    ]
