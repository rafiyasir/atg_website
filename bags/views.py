from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Bag
from pages.models import Page

def index(request):
    bags = Bag.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(bags, 6)
    page = request.GET.get('page')
    paged_bags = paginator.get_page(page)

    context = {
        'bags' : paged_bags
    }

    return render(request, 'bags/bags.html', context)

def bag(request,bag_id):
    bag = get_object_or_404(Bag, pk=bag_id)
    support = Page.objects.all()

    context = {
        'bag' : bag,
        'support':support
    }
    return render(request, 'bags/bag.html', context)