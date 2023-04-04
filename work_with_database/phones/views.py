from django.shortcuts import render, redirect
from phones.models import Phone
from django.http import HttpResponse

def index(request):
    return redirect('catalog')

def store(request):
    phones = Phone.objects.all()
    template = 'catalog.html'
    # phones = [f'{c.id}, {c.name}, {c.price}, {c.image}, {c.release_date}' for c in phone]
    # return HttpResponse('<br>'.join(phones))
    for phone in phones:
        context = {'phone': phone}

    return render(request, template, context)


def show_catalog(request):
    template = 'catalog.html'
    phone = Phone.objects.all()
    context = {'phone': phone}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.all()
    context = {'phone': phone}
    return render(request, template, context)
