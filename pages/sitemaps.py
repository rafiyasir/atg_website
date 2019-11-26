from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from bags.models import Bag
from promotionals.models import Promotional
from miscellaneous.models import Miscellaneous

class StaticSitemap(Sitemap):

    def items(self):
        return ['index','about','products','clients','contactus','register','login','dashboard','logout']

    def location(self, item):
        return reverse(item)



class BagSitemap(Sitemap):

    def items(self):
        return Bag.objects.all()

class PromoSitemap(Sitemap):

    def items(self):
        return Promotional.objects.all()

class MiscSitemap(Sitemap):

    def items(self):
        return Miscellaneous.objects.all()


