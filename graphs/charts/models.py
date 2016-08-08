from __future__ import unicode_literals

from django.db import models

# Create your models here.


class CountryModel(models.Model):
    country = models.CharField(null=False,max_length=200)
    population = models.CharField(max_length=1000)
    life_expectancy = models.CharField(max_length=1000)
    density = models.CharField(max_length=1000)
    literacy = models.CharField(max_length=1000)
