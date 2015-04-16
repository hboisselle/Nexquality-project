# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Nexquality', '0016_auto_20150415_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='conditions_code',
            field=models.CharField(max_length=4000, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='badgeuser',
            name='attribution_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 16, 13, 55, 9, 317723, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 16, 13, 55, 9, 307534, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='in_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 16, 13, 55, 9, 314621, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
