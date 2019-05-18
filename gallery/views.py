from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def new(request):
    return HttpResponse("<h2>Welcome to gallery</h2>")