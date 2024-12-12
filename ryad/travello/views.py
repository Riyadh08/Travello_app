# Controller eita kaj kore
from django.shortcuts import render
from .models import Destination

def index(request):
    

    dests = Destination.objects.all()

    return render(request, 'index.html',{'dests':dests})

def about(request):
    return render(request, 'about.html')

def news(request):
    return render(request, 'news.html')

def contact(request):
    return render(request, 'contact.html')