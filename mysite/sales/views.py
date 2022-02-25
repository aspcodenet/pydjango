from django.shortcuts import render
from django.http import HttpResponse
from .models import Car

# Create your views here.
def index(request):
    cars = Car.objects.order_by('price')
    context = {'allCars': cars,
                'Rubriken': 'Hejsan'
    }
    return render(request, 'sales/index.html', context)




def onecar(request, id):
    return HttpResponse("You're looking at car %s." % id)    
