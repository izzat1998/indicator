from django.shortcuts import render

# Create your views here.
# Create your models here.
from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = 'dashboard.html'
