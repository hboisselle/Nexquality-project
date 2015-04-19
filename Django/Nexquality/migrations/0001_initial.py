# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings
import conditions.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('conditions', conditions.fields.ConditionsField(default=dict)),
                ('image', models.ImageField(upload_to=b'images/badges')),
                ('score', models.IntegerField(default=0)),
                ('given_once', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BadgeCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BadgeUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attribution_date', models.DateTimeField(default=datetime.datetime(2015, 4, 19, 3, 50, 48, 222563, tzinfo=utc))),
                ('removal_date', models.DateField(null=True, blank=True)),
                ('badge', models.ForeignKey(to='Nexquality.Badge')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-attribution_date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('revision', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('comment', models.CharField(max_length=500)),
                ('code_review_score', models.FloatField(null=True)),
            ],
            options={
                'ordering': ['-revision'],
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
                ('calculated', models.FloatField(null=True)),
                ('commit', models.ForeignKey(to='Nexquality.Commit')),
            ],
            options={
                'ordering': ['field'],
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
                ('unit', models.CharField(max_length=50, null=True, blank=True)),
                ('show_color', models.BooleanField(default=False)),
                ('show_plus_sign', models.BooleanField(default=False)),
                ('tolerance', models.FloatField(default=0)),
                ('reverse_tolerance', models.BooleanField(default=False)),
                ('show_average', models.BooleanField(default=True)),
                ('show_sum', models.BooleanField(default=True)),
                ('category', models.ForeignKey(to='Nexquality.MetricCategory')),
            ],
            options={
                'ordering': ['category', 'name'],
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
                ('start_date', models.DateField(default=datetime.datetime(2015, 4, 19, 3, 50, 48, 213756, tzinfo=utc))),
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
                ('in_date', models.DateField(default=datetime.datetime(2015, 4, 19, 3, 50, 48, 224462, tzinfo=utc))),
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
        migrations.AddField(
            model_name='badge',
            name='category',
            field=models.ForeignKey(default=1, to='Nexquality.BadgeCategory'),
            preserve_default=True,
        ),
    ]
