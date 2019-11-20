from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Promotional
from pages.models import Page

def index(request):
    promos = Promotional.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(promos, 2)
    page = request.GET.get('page')
    paged_promos = paginator.get_page(page)

    context = {
        'promos' : paged_promos
    }

    return render(request, 'promotionals/promotionals.html', context)

def promotional(request, promotional_id):
    promo = get_object_or_404(Promotional, pk=promotional_id)
    support = Page.objects.all()

    context = {
        'promo' : promo,
        'support':support
    }

    return render(request, 'promotionals/promotional.html', context)
