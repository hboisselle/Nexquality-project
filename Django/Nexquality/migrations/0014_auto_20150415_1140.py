# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Nexquality', '0013_auto_20150414_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='commit',
            name='code_review_score',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 15, 15, 40, 52, 998355, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='in_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 15, 15, 40, 52, 999520, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
