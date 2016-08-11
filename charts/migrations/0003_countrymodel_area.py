# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0002_auto_20160808_0714'),
    ]

    operations = [
        migrations.AddField(
            model_name='countrymodel',
            name='area',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
