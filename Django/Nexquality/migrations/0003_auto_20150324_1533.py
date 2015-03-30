# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Nexquality', '0002_auto_20150324_0951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectuser',
            name='joined_date',
        ),
        migrations.AddField(
            model_name='projectuser',
            name='in_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 24, 19, 33, 51, 251805, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='projectuser',
            name='out_date',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 24, 19, 33, 51, 250782, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
