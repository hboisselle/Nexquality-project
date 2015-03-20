# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Nexquality', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='project',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='Nexquality.ProjectTeam'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='projectteam',
            name='joined_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 20, 14, 12, 12, 778366, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='projectteam',
            name='role',
            field=models.ForeignKey(default=1, to='Nexquality.ProjectRole'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 20, 14, 12, 12, 777465, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
