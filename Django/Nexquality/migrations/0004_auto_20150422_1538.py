# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Nexquality', '0003_auto_20150418_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badgeuser',
            name='attribution_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 22, 19, 38, 9, 512203, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 22, 19, 38, 9, 501247, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='in_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 22, 19, 38, 9, 511510, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
