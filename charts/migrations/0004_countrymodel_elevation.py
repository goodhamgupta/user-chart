# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0003_countrymodel_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='countrymodel',
            name='elevation',
            field=models.CharField(default=0, max_length=1000),
        ),
    ]
