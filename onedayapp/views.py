from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Contact
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactSerializers
from datetime import datetime
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


def copyrights(request):
    tempiate=loader.get_template('copyrights.html')
    return HttpResponse(tempiate.render())

from django.utils import timezone

@api_view(['POST'])
def contact_POST(request):
    if request.method == 'POST':
        serializer = ContactSerializers(data=request.data)
        if serializer.is_valid():
            user_data=serializer.validated_data
            now = timezone.now().isoformat()
            print("now =", now)
            user_data['Uploded_time']=now
            serializer.save()
            return Response({"message": "Contact created successfully!", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def contact_GET(request ,pk):
    if request.method=='GET':
        user_profiles =Contact.objects.get(pk=pk)
        return Response({"message": "Contact created successfully!", "data": user_profiles}, status=status.HTTP_201_CREATED)