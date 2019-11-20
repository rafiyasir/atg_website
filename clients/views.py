from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Client

def client(request):
    clients = Client.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(clients, 6)
    page = request.GET.get('page')
    paged_clients = paginator.get_page(page)

    context = {
        'clients' : paged_clients
    }

    return render(request,'clients/clients.html', context)
