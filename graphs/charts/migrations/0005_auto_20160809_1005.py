# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0004_countrymodel_elevation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContinentModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('continent', models.CharField(max_length=200)),
                ('population', models.CharField(max_length=1000)),
                ('life_expectancy', models.CharField(default=0, max_length=1000)),
                ('area', models.CharField(default=0, max_length=100)),
                ('density', models.CharField(default=0, max_length=1000)),
                ('elevation', models.CharField(default=0, max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='countrymodel',
            name='literacy',
        ),
    ]
