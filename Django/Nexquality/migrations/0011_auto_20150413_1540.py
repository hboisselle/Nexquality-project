# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Nexquality', '0010_auto_20150413_1521'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='metric',
            options={'ordering': ['field']},
        ),
        migrations.AlterModelOptions(
            name='metricfield',
            options={'ordering': ['category', 'name']},
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 13, 19, 40, 10, 237192, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='in_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 13, 19, 40, 10, 239104, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
