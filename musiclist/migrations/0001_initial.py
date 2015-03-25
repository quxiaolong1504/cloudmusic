# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', help_text='\u6b4c\u5355\u540d\u79f0', max_length=100)),
                ('create_at', models.DateTimeField(help_text='\u521b\u5efa\u65f6\u95f4', auto_now_add=True)),
                ('listen_count', models.IntegerField(default=0, help_text='\u6536\u542c\u6570')),
                ('introduction', models.CharField(help_text='\u6b4c\u5355\u7b80\u4ecb', max_length=200)),
                ('master', models.ForeignKey(related_name='music_lists', to=settings.AUTH_USER_MODEL, help_text='\u6b4c\u5355\u7528\u8005')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='\u6807\u7b7e\u540d\u79f0', max_length=20)),
                ('user', models.ForeignKey(related_name='tags', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='musiclist',
            name='tags',
            field=models.ManyToManyField(help_text='\u6807\u7b7e\u5217\u8868', related_name='music_lists', to='musiclist.Tag'),
            preserve_default=True,
        ),
    ]
