# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Nexquality', '0020_auto_20150330_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('revision', models.IntegerField()),
                ('date', models.DateField()),
                ('comment', models.CharField(max_length=500)),
                ('metrics', models.OneToOneField(to='Nexquality.Metrics')),
                ('project', models.ForeignKey(to='Nexquality.Project')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='commits',
            name='user',
        ),
        migrations.DeleteModel(
            name='Commits',
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
            field=models.DateField(default=datetime.datetime(2015, 4, 1, 13, 45, 42, 168978, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='in_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 1, 13, 45, 42, 170133, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
