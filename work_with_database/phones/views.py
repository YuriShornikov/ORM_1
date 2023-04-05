from django.shortcuts import render, redirect
from phones.models import Phone
from django.http import HttpResponse

def index(request):
    return redirect('catalog')

def show_catalog(request):

    template = 'catalog.html'

    if request.GET['sort'] == 'name':
        phones = Phone.objects.order_by('name')
    elif request.GET['sort'] == 'min_price':
        phones = Phone.objects.order_by('price')
    elif request.GET['sort'] == 'max_price':
        phones = Phone.objects.order_by('-price')
    else:
        phones = Phone.objects.all()

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.all()
    for phone in phones:
        if slug == phone.slug:
            context = {'phone': phone}
            print(phone)
            return render(request, template, context)
