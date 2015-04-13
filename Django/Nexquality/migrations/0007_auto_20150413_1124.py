# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Nexquality', '0006_auto_20150413_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='metricfield',
            name='reverse_tolerance',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 13, 15, 24, 29, 851609, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='in_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 13, 15, 24, 29, 852953, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
