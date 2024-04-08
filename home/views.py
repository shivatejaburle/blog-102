from django.shortcuts import render
from django.views.generic import TemplateView

# Home Page View
class HomePage(TemplateView):
    template_name = 'home/index.html'