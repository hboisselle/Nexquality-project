# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Nexquality', '0009_auto_20150413_1346'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commit',
            options={'ordering': ['-revision']},
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 13, 19, 21, 55, 545405, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='in_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 13, 19, 21, 55, 548007, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
