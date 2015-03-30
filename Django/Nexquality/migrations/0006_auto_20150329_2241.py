# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Nexquality', '0005_auto_20150327_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 30, 2, 41, 25, 465020, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='in_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 30, 2, 41, 25, 466006, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='projectuser',
            unique_together=set([]),
        ),
    ]
