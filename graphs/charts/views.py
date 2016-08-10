from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import viewsets
import requests
from models import CountryModel, ContinentModel
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
    return render(request,"home.html")

def detail(request):
    return render(request,"detail.html")


@api_view(['GET'])
def get_country_data(request,data):
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
                data_list.append(obj.elevation)
        elif data == 5:
            for obj in objects:
                country_list.append(obj.country)
                data_list.append(obj.density)
        final_list = [country_list,data_list]
    except Exception as e:
        print "ERROR OCCURED! ",e

    return Response(final_list)

@api_view(['GET'])
def get_continent_data(request,data):
    data = int(data)
    objects = ContinentModel.objects.all()
    country_list = []
    data_list = []
    final_list = []
    try:
        if data == 1:
            for obj in objects:
                country_list.append(obj.continent)
                data_list.append(obj.population)
        elif data == 2:
            for obj in objects:
                country_list.append(obj.continent)
                data_list.append(obj.life_expectancy)
        elif data == 3:
            for obj in objects:
                country_list.append(obj.continent)
                data_list.append(obj.area)
        elif data == 4:
            for obj in objects:
                country_list.append(obj.continent)
                data_list.append(obj.elevation)
        elif data == 5:
            for obj in objects:
                country_list.append(obj.continent)
                data_list.append(obj.density)
        final_list = [country_list,data_list]
    except Exception as e:
        print "ERROR OCCURED! ",e

    return Response(final_list)

@api_view(['GET'])
def get_country_detail(request,param1,param2):
    param1 = int(param1)
    param2 = int(param2)
    objects = CountryModel.objects.all()
    first_data_list = []
    second_data_list = []
    final_list = []
    try:
        if param1 == 1:
            param1 = 'population'
        elif param1 == 2:
            param1 = 'life_expectancy'
        elif param1 == 3:
            param1 = 'area'
        elif param1 == 4:
            param1 = 'density'
        elif param1 == 5:
            param1 = 'elevation'

        if param2 == 1:
            param2 = 'population'
        elif param2 == 2:
            param2 = 'life_expectancy'
        elif param2 == 3:
            param2 = 'area'
        elif param2 == 4:
            param2 = 'elevation'
        elif param2 == 5:
            param2 = 'density'

        for obj in objects:
            first_data_list.append(getattr(obj,param1))
            second_data_list.append(getattr(obj,param2))
        final_list = [first_data_list,second_data_list]
        print final_list
    except Exception as e:
        print "ERROR OCCURED! ",e

    return Response(final_list)

@api_view(['GET'])
def get_continent_detail(request,param1,param2):
    param1 = int(param1)
    param2 = int(param2)
    objects = ContinentModel.objects.all()
    first_data_list = []
    second_data_list = []
    final_list = []
    try:
        if param1 == 1:
            param1 = 'population'
        elif param1 == 2:
            param1 = 'life_expectancy'
        elif param1 == 3:
            param1 = 'area'
        elif param1 == 4:
            param1 = 'elevation'
        elif param1 == 5:
            param1 = 'density'

        if param2 == 1:
            param2 = 'population'
        elif param2 == 2:
            param2 = 'life_expectancy'
        elif param2 == 3:
            param2 = 'area'
        elif param2 == 4:
            param2 = 'elevation'
        elif param2 == 5:
            param2 = 'density'

        for obj in objects:
            print "KERE"
            first_data_list.append(getattr(obj,param1))
            second_data_list.append(getattr(obj,param2))

        final_list = [first_data_list,second_data_list]
        print final_list
    except Exception as e:
        print "ERROR OCCURED! ",e

    return Response(final_list)