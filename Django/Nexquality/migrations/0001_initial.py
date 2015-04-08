# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('revision', models.IntegerField()),
                ('date', models.DateField()),
                ('comment', models.CharField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Complexity',
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
            name='Coverage',
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
            name='Duplication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('duplicated_blocks', models.IntegerField()),
                ('duplicated_lines', models.IntegerField()),
                ('duplicated_lines_density', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IssueLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Metrics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('complexity', models.OneToOneField(to='Nexquality.Complexity')),
                ('coverage', models.OneToOneField(to='Nexquality.Coverage')),
                ('duplication', models.OneToOneField(to='Nexquality.Duplication')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rank', models.IntegerField(default=1)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=250)),
                ('start_date', models.DateField(default=datetime.datetime(2015, 4, 4, 18, 40, 41, 287283, tzinfo=utc))),
                ('is_done', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(related_name='project_starts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('in_date', models.DateField(default=datetime.datetime(2015, 4, 4, 18, 40, 41, 288439, tzinfo=utc))),
                ('out_date', models.DateField(null=True, blank=True)),
                ('project', models.ForeignKey(to='Nexquality.Project')),
            ],
            options={
                'ordering': ['out_date', 'in_date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectUserRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Violation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='projectuser',
            name='role',
            field=models.ForeignKey(default=1, to='Nexquality.ProjectUserRole'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='projectuser',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='Nexquality.ProjectUser'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='issue',
            name='level',
            field=models.ForeignKey(to='Nexquality.IssueLevel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='issue',
            name='violation',
            field=models.ForeignKey(to='Nexquality.Violation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='commit',
            name='issues',
            field=models.ManyToManyField(to='Nexquality.Issue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='commit',
            name='metrics',
            field=models.OneToOneField(to='Nexquality.Metrics'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='commit',
            name='project',
            field=models.ForeignKey(to='Nexquality.Project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='commit',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
