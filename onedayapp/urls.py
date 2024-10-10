from django.contrib import admin
from django.urls import path, include
from .views import contact_POST
from . import views
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('services', views.services, name='services'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contactus', views.contactus, name='contactus'),
    path('copyrights', views.copyrights, name='copyrights'),
    path('api/contact_POST', views.contact_POST, name='contact_POST'),
    path('api/contact_GET/<int:pk>/', views.contact_GET, name='contact_GET'),

]