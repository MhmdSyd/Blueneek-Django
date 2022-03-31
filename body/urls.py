from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('',home),
    path('index.html', index),
    path('about.html', about),
    path('clients.html', clients),
    path('ourwork.html', ourwork),
    path('contact.html', contact),
    
]