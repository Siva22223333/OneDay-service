from rest_framework import serializers
from .models import Contact

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['Name', 'Email', 'Message','Uploded_time']