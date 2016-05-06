from django.shortcuts import render, redirect
from collection.forms import AktivitetForm
from collection.models import Aktiviteter

def index(request):
    aktivitet = Aktiviteter.objects.all()
    return render(request, 'index.html', {'aktivitet': aktivitet,})

def aktivitet_detail(request, slug):
    aktivitet = Aktiviteter.objects.get(slug=slug)
    return render(request, 'aktivitet/aktivitet_detail.html', {'aktivitet': aktivitet,})

def edit_aktivitet(request, slug):
    aktivitet = Aktiviteter.objects.get(slug=slug)
    form_class = AktivitetForm

    if request.method == 'POST':
        form = form_class(data=request.POST, instance=aktivitet)
        if form.is_valid():
            form.save()
            return redirect('aktivitet_detail', slug=aktivitet.slug)
    else:
        form = form_class(instance=aktivitet)
    return render(request,'aktivitet/edit_aktivitet.html', {'aktivitet':aktivitet, 'form':form,})        

# def index(request):
#     number = 6
#     thing = "thing"
#     return render(request, 'index.html',{'number': number, 'thing': thing})  
