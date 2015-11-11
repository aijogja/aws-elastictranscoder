# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import video.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('video', models.FileField(max_length=250, upload_to=video.models.get_video_file_path)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Video',
            },
        ),
    ]
