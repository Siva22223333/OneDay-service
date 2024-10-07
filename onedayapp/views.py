from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.
def dashboard(request):
    tempiate=loader.get_template('dashboard.html')
    return HttpResponse(tempiate.render())