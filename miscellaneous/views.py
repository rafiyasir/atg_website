from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Miscellaneous
from pages.models import Page

def index(request):
    items = Miscellaneous.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(items, 2)
    page = request.GET.get('page')
    paged_items = paginator.get_page(page)

    context = {
        'items' : paged_items
    }

    return render(request, 'miscellaneous/misc_items.html', context)

def miscellaneous(request, miscellaneous_id):
    misc = get_object_or_404(Miscellaneous, pk=miscellaneous_id)
    support = Page.objects.all()

    context = {
        'misc' : misc,
        'support':support
    }

    return render(request, 'miscellaneous/misc_item.html', context)
