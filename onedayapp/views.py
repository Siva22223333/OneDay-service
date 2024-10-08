from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.
def dashboard(request):
    tempiate=loader.get_template('dashboard.html')
    return HttpResponse(tempiate.render())

def services(request):
    tempiate=loader.get_template('services.html')
    return HttpResponse(tempiate.render())


def aboutus(request):
    tempiate=loader.get_template('aboutus.html')
    return HttpResponse(tempiate.render())


def contactus(request):
    tempiate=loader.get_template('contactus.html')
    return HttpResponse(tempiate.render())

