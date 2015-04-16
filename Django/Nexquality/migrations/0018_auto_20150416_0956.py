# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Nexquality', '0017_auto_20150416_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='conditions_code',
            field=models.CharField(max_length=4000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='badgeuser',
            name='attribution_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 16, 13, 56, 38, 971481, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 16, 13, 56, 38, 961350, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='in_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 16, 13, 56, 38, 968649, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
