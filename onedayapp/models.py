from django.db import models

# Create your models here.

class Contact(models.Model):
    Name=models.CharField( max_length=50,null=True)
    Email=models.CharField( max_length=50,null=True)
    Message=models.TextField(null=True)
    Uploded_time=models.DateTimeField(auto_now=False, auto_now_add=False ,null=True)
