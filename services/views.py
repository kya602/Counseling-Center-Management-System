from django.shortcuts import render
from .models import Service
from django.template import loader
from django.http import HttpResponse



def index(request):
    all_services = Service.objects.all()
    template = loader.get_template('services/services.html')
    context = {
        'all_services': all_services,
    }
    return HttpResponse(template.render(context,request))



