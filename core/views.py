from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class homeview(TemplateView):
    template_name = 'index.html'

class Contactview(TemplateView):
    template_name = 'contact_us.html'
