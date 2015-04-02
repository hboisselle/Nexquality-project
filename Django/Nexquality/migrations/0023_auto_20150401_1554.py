# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Nexquality', '0022_auto_20150401_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complexitymetrics',
            name='average_by_method',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coveragemetrics',
            name='code_coverage',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coveragemetrics',
            name='number_of_failing_tests',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coveragemetrics',
            name='number_of_ignored_tests',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coveragemetrics',
            name='number_of_tests',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='duplicationmetrics',
            name='duplicated_blocks',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='duplicationmetrics',
            name='duplicated_lines',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='duplicationmetrics',
            name='duplicated_lines_density',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 1, 19, 54, 58, 898879, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='in_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 1, 19, 54, 58, 900031, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
