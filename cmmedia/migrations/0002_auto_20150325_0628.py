# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmmedia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='\u4e13\u8f91\u540d', max_length=50)),
                ('thumbnail', models.ImageField(null=True, upload_to=b'albums/thumbail/', blank=True)),
                ('publishing_at', models.DateTimeField(help_text='\u53d1\u884c\u65f6\u95f4', auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='\u59d3\u540d', max_length=50)),
                ('head_photo', models.ImageField(default=None, max_length=255, null=True, upload_to=b'artists/head_photo/', blank=True)),
                ('gender', models.CharField(max_length=10, choices=[(b'male', b'male'), (b'female', b'female')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', help_text='\u6b4c\u540d', max_length=50)),
                ('file', models.FileField(default=None, help_text='\u97f3\u4e50\u6587\u4ef6', upload_to=b'musics/')),
                ('duration', models.CharField(default=b'', help_text='\u6b4c\u66f2\u65f6\u957f', max_length=30)),
                ('albums', models.ForeignKey(related_name='musics', default=None, to='cmmedia.Album', help_text='\u6240\u5c5e\u4e13\u8f91')),
                ('artists', models.ManyToManyField(default=None, help_text='\u6f14\u5531\u8005', to='cmmedia.Artist', related_name='musics')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.ImageField(upload_to=b'cmmedia'),
            preserve_default=True,
        ),
    ]
