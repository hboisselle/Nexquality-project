# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Nexquality', '0009_auto_20150330_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 30, 16, 56, 49, 152174, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='in_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 30, 16, 56, 49, 153163, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
