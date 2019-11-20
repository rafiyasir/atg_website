from django.shortcuts import render

from .models import Page
from clients.models import Client

def index(request):
    contents = Page.objects.all()
    context = {
        'contents' : contents
    }

    return render(request, 'pages/index.html', context)

def about(request):
    contents = Page.objects.all()
    clients = Client.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'contents' : contents,
        'clients' : clients
    }

    return render(request, 'pages/about.html', context)

def products(request):
    contents = Page.objects.all()
    
    context = {
        'contents' : contents
    }

    return render(request, 'pages/products.html', context)

def search(request):
    return render(request, 'pages/search.html')
