from django.shortcuts import render
from collection.models import Aktiviteter

def index(request):
    aktivitet = Aktiviteter.objects.all()
    return render(request, 'index.html', {'aktivitet': aktivitet,})


# def index(request):
#     number = 6
#     thing = "thing"
#     return render(request, 'index.html',{'number': number, 'thing': thing})  
