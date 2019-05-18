from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def new(request):
    template = loader.get_template('file.html')
    return HttpResponse(template.render())
