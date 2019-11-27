from bags.models import Bag
from promotionals.models import Promotional
from miscellaneous.models import Miscellaneous

def products_dropdown(request):
    drpdwn_bags = Bag.objects.all().filter(is_published=True)
    drpdwn_promos = Promotional.objects.all().filter(is_published=True)
    drpdwn_miscs = Miscellaneous.objects.all().filter(is_published=True)

    context = {
        'drpdwn_bags':drpdwn_bags,
        'drpdwn_promos':drpdwn_promos,
        'drpdwn_miscs':drpdwn_miscs
    }
    return context