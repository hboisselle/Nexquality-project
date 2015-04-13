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
                ('date', models.DateTimeField()),
                ('comment', models.CharField(max_length=500)),
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
            name='Metric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.FloatField()),
                ('commit', models.ForeignKey(to='Nexquality.Commit')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MetricCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MetricField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('unit', models.CharField(max_length=50, null=True)),
                ('category', models.ForeignKey(to='Nexquality.MetricCategory')),
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
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProfileType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
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
                ('start_date', models.DateField(default=datetime.datetime(2015, 4, 11, 21, 10, 3, 404304, tzinfo=utc))),
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
                ('in_date', models.DateField(default=datetime.datetime(2015, 4, 11, 21, 10, 3, 405353, tzinfo=utc))),
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
            model_name='profile',
            name='profiletype',
            field=models.ForeignKey(default=1, to='Nexquality.ProfileType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='metric',
            name='field',
            field=models.ForeignKey(to='Nexquality.MetricField'),
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
