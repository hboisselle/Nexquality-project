# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Nexquality', '0007_auto_20150329_2352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commits',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('revision', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('comment', models.CharField(max_length=500)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ComplexityMetrics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('complexity', models.FloatField()),
                ('average_by_class', models.FloatField()),
                ('average_by_method', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoverageMetrics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('line_of_code', models.IntegerField()),
                ('number_of_tests', models.IntegerField()),
                ('number_of_failing_tests', models.IntegerField()),
                ('number_of_ignored_tests', models.IntegerField()),
                ('code_coverage', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DuplicationMetrics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('duplicated_blocks', models.IntegerField()),
                ('duplicated_lines', models.IntegerField()),
                ('duplicated_lines_density', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Metrics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('complexity', models.ForeignKey(to='Nexquality.ComplexityMetrics')),
                ('coverage', models.ForeignKey(to='Nexquality.CoverageMetrics')),
                ('duplication', models.ForeignKey(to='Nexquality.DuplicationMetrics')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 30, 14, 38, 10, 903358, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='in_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 30, 14, 38, 10, 904443, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
