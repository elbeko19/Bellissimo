from django.shortcuts import render
from .models import Pizza

def index(request):
    pics = Pizza.objects.all()
    return render(request, 'index.html', {'pics': pics})



def pizza(request):
    pics = Pizza.objects.all()
    return render(request, 'pizza.html', {'pics': pics})
