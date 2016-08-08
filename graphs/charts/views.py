from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import viewsets
import requests

app_id = "5f68be87"
app_key = "a5699ef989e61a480601bc60f022f559"
def get_data(request):
    r=requests.get("http://api.undata-api.org/organizations?app_id={"+app_id+"}&app_key={"+app_key+"}")
    print r.content

def chart(request):
    print "Rendering"
    #return Response({"extra":"extra"},template_name="/static/charts/test.html")
    return render(request,"charts/test.html")

