# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Nexquality', '0012_auto_20150413_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='metricfield',
            name='show_average',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='metricfield',
            name='show_sum',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 14, 13, 12, 37, 156305, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='in_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 14, 13, 12, 37, 157344, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
