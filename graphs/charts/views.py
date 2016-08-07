from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import viewsets


def chart(request):
    print "Rendering"
    #return Response({"extra":"extra"},template_name="/static/charts/test.html")
    return render(request,"static/charts/test.html")

