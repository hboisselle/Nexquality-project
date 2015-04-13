# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Nexquality', '0002_auto_20150411_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='metricfield',
            name='color_showing_tolerance',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 11, 21, 30, 2, 961976, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='in_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 11, 21, 30, 2, 963187, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
