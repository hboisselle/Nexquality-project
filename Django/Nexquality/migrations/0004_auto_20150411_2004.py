# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Nexquality', '0003_auto_20150411_1730'),
    ]

    operations = [
        migrations.RenameField(
            model_name='metricfield',
            old_name='color_showing_tolerance',
            new_name='tolerance',
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 12, 0, 4, 16, 254308, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='in_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 12, 0, 4, 16, 255325, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
