# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Nexquality', '0004_auto_20150422_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='name',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='badgeuser',
            name='attribution_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 27, 19, 16, 9, 793773, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 27, 19, 16, 9, 779745, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='in_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 27, 19, 16, 9, 792895, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
