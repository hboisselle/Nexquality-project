# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Nexquality', '0023_auto_20150401_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metrics',
            name='complexity',
            field=models.OneToOneField(null=True, to='Nexquality.ComplexityMetrics'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='metrics',
            name='coverage',
            field=models.OneToOneField(null=True, to='Nexquality.CoverageMetrics'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='metrics',
            name='duplication',
            field=models.OneToOneField(null=True, to='Nexquality.DuplicationMetrics'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 1, 19, 57, 21, 487368, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='in_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 1, 19, 57, 21, 488549, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
