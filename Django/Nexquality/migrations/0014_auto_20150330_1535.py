# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Nexquality', '0013_auto_20150330_1408'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectuser',
            options={'ordering': ['out_date']},
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 30, 19, 35, 12, 206595, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='in_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 30, 19, 35, 12, 207650, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
