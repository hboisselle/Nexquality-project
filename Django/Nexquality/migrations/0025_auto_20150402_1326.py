# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Nexquality', '0024_auto_20150401_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complexitymetrics',
            name='average_by_method',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coveragemetrics',
            name='code_coverage',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coveragemetrics',
            name='number_of_failing_tests',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coveragemetrics',
            name='number_of_ignored_tests',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coveragemetrics',
            name='number_of_tests',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='duplicationmetrics',
            name='duplicated_blocks',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='duplicationmetrics',
            name='duplicated_lines',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='duplicationmetrics',
            name='duplicated_lines_density',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='metrics',
            name='complexity',
            field=models.OneToOneField(to='Nexquality.ComplexityMetrics'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='metrics',
            name='coverage',
            field=models.OneToOneField(to='Nexquality.CoverageMetrics'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='metrics',
            name='duplication',
            field=models.OneToOneField(to='Nexquality.DuplicationMetrics'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 2, 17, 25, 49, 250811, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='in_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 2, 17, 25, 49, 251962, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
