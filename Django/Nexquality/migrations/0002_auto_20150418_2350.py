# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Nexquality', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badgeuser',
            name='attribution_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 19, 3, 50, 52, 398893, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 19, 3, 50, 52, 389143, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='in_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 19, 3, 50, 52, 400947, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
