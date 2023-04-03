from django.shortcuts import render, redirect
from phones.management.commands.import_phones import Command
from django.http import HttpResponse

def index(request):
    return redirect('catalog')


# def csv_c(request):
#     Command.create_parser()
#     return HttpResponse(f'succes')

def show_catalog(request):
    template = 'catalog.html'
    context = {}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
