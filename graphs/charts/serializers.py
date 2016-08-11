from rest_framework import serializers
from charts.models import CountryModel, ContinentModel

class ContinentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContinentModel
        fields = ('continent', 'population', 'life_expectancy', 'area', 'density', 'elevation')

class CountryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryModel
        fields = ('country', 'population', 'life_expectancy', 'area', 'density', 'elevation')
