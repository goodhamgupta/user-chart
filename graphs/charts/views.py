from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import viewsets
import requests
from models import CountryModel

# app_id = "5f68be87"
# app_key = "a5699ef989e61a480601bc60f022f559"
# def get_data(request):
#     r=requests.get("http://api.undata-api.org/organizations?app_id={"+app_id+"}&app_key={"+app_key+"}")
#     print r.content

def chart(request):
    #return Response({"extra":"extra"},template_name="/static/charts/test.html")
    country_objs = CountryModel.objects.all()
    return render(request,"charts/test.html",{ "data" : country_objs})


@api_view(['GET'])
def get_data(request,data):
    object = []
    data = int(data)
    if data == 1:
        print "Here"
        object = CountryModel.objects.values_list('country','population')
        print len(object)
    elif data == 2:
        object = CountryModel.objects.values_list('country','life_expectancy')
    elif data == 3:
        object = CountryModel.objects.values_list('country','area')
    elif data == 4:
        object = CountryModel.objects.values_list('country','density')
    elif data == 5:
        object = CountryModel.objects.values_list('country','elevation')

    return Response(object)