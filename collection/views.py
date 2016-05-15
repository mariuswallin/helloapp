from django.shortcuts import render, redirect
from collection.forms import AktivitetForm
from collection.models import Aktiviteter
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404

def index(request):
    aktivitet = Aktiviteter.objects.all()
    return render(request, 'index.html', {'aktivitet': aktivitet,})

def aktivitet_detail(request, slug):
    aktivitet = Aktiviteter.objects.get(slug=slug)
    return render(request, 'aktivitet/aktivitet_detail.html', {'aktivitet': aktivitet,})

@login_required
def edit_aktivitet(request, slug):
    aktivitet = Aktiviteter.objects.get(slug=slug)
    form_class = AktivitetForm

    if aktivitet.user != request.user:
        raise Http404

    if request.method == 'POST':
        form = form_class(data=request.POST, instance=aktivitet)
        if form.is_valid():
            form.save()
            return redirect('aktivitet_detail', slug=aktivitet.slug)
    else:
        form = form_class(instance=aktivitet)
    return render(request,'aktivitet/edit_aktivitet.html', {'aktivitet':aktivitet, 'form':form,})   

def create_aktivitet(request):
    form_class = AktivitetForm

    if request.method == 'POST':
        form = form_class(request.POST)

        if form.is_valid():
            aktivitet = form.save(commit=False)
            aktivitet.user = request.user
            aktivitet.slug = slugify(aktivitet.name)
            aktivitet.save()
            return redirect('aktivitet_detail', slug=aktivitet.slug)
    else:
        form = form_class()
    return render(request,'aktivitet/create_aktivitet.html', {'form':form,})   

def browse_by_name(request, initial=None):
    if initial:
        aktivitet = Aktiviteter.objects.filter(name__istartswith=initial)
        aktivitet = aktivitet.order_by('name')
    else:
        aktivitet = Aktiviteter.objects.all().order_by('name')

    return render(request,'search/search.html', {'aktivitet':aktivitet, 'initial': initial,})              

# def index(request):
#     number = 6
#     thing = "thing"
#     return render(request, 'index.html',{'number': number, 'thing': thing})  
