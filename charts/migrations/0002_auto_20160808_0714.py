# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='countrymodel',
            name='life_expectancy',
            field=models.CharField(default=0, max_length=1000),
        ),
        migrations.AlterField(
            model_name='countrymodel',
            name='density',
            field=models.CharField(default=0, max_length=1000),
        ),
        migrations.AlterField(
            model_name='countrymodel',
            name='literacy',
            field=models.CharField(default=0, max_length=1000),
        ),
    ]
