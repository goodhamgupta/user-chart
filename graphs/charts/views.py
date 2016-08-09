from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import viewsets
import requests
from models import CountryModel
from charts.vars import population,population_density,life_expectancy,elevation,surface_area

# app_id = "5f68be87"
# app_key = "a5699ef989e61a480601bc60f022f559"
# def get_data(request):
#     r=requests.get("http://api.undata-api.org/organizations?app_id={"+app_id+"}&app_key={"+app_key+"}")
#     print r.content

@api_view(['GET'])
def insert_data(request):

    for obj in population:
        country = obj['country']
        population = obj['population']
        b = CountryModel(country=country,population=population)
        b.save()
    for obj in life_expectancy:
        try:
            b = CountryModel.objects.get(country=obj['country'])
            b.life_expectancy = obj['expectancy']
            b.save()
        except Exception as e:
            continue

    for obj in surface_area:
            try:
                b = CountryModel.objects.get(country=obj['country'])
                b.area = obj['area']
                b.save()
            except:
                continue

    for obj in population_density:
            try:
                b = CountryModel.objects.get(country=obj['country'])
                b.density = obj['density']
                b.save()
            except Exception as e:
                continue

    for obj in elevation:
            try:
                b = CountryModel.objects.get(country=obj['country'])
                den = obj['average'][:-1]
                b.elevation = den
                b.save()
            except Exception as e:
                continue
    return Response("Complete")

def chart(request):
    #return Response({"extra":"extra"},template_name="/static/charts/base.html")
    return render(request,"base.html")


@api_view(['GET'])
def get_data(request,data):
    object = []
    data = int(data)
    objects = CountryModel.objects.all()
    country_list = []
    data_list = []
    final_list = []
    try:
        if data == 1:
            for obj in objects:
                country_list.append(obj.country)
                data_list.append(obj.population)
        elif data == 2:
            for obj in objects:
                country_list.append(obj.country)
                data_list.append(obj.life_expectancy)
        elif data == 3:
            for obj in objects:
                country_list.append(obj.country)
                data_list.append(obj.area)
        elif data == 4:
            for obj in objects:
                country_list.append(obj.country)
                data_list.append(obj.density)
        elif data == 5:
            for obj in objects:
                country_list.append(obj.country)
                data_list.append(obj.elevation)
        final_list = [country_list,data_list]
    except Exception as e:
        print "ERROR OCCURED! ",e

    return Response(final_list)