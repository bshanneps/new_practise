from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

data = {
    "name": "Ram"
}

names_dict = {
   "names": [
    "ram",
    "shyam",
    "hari",
    "krishna"
   ]
}

def abc(request):
    return HttpResponse("<h2>You just visited empty Path</h>")    

def msg(request):
    return HttpResponse("<h2>You just visited message path</h2>")

def temp_example(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(data))

def show_names(request):
    template = loader.get_template('names.html')
    return HttpResponse(template.render(names_dict))

def ink(request):
    template = loader.get_template('layout_template.html')
    return HttpResponse(template.render(data))

