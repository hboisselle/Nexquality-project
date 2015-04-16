# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Nexquality', '0015_auto_20150415_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('conditions_code', models.CharField(max_length=4000)),
                ('image', models.ImageField(upload_to=b'images/badges')),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BadgeUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attribution_date', models.DateField(default=datetime.datetime(2015, 4, 16, 1, 12, 55, 410963, tzinfo=utc))),
                ('removal_date', models.DateField(null=True, blank=True)),
                ('attributed_by', models.ForeignKey(related_name='badge_attributed_by', to=settings.AUTH_USER_MODEL)),
                ('badge', models.ForeignKey(to='Nexquality.Badge')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 16, 1, 12, 55, 399046, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='in_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 16, 1, 12, 55, 406843, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
