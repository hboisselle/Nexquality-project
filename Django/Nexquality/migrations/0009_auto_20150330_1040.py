# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Nexquality', '0008_auto_20150330_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commits',
            name='revision',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 30, 14, 40, 51, 858213, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='in_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 30, 14, 40, 51, 859481, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
