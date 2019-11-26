
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from pages.sitemaps import BagSitemap, StaticSitemap, PromoSitemap, MiscSitemap

sitemaps = {
    'static': StaticSitemap,
    'bags': BagSitemap,
    'promo': PromoSitemap,
    'misc': MiscSitemap
}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}),
    path('miscellaneous/',include('miscellaneous.urls')),
    path('promotionals/',include('promotionals.urls')),
    path('bags/',include('bags.urls')),
    path('clients/',include('clients.urls')),
    path('',include('pages.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
    path('contactsp/', include('contactsP.urls')),
    path('contactsm/', include('contactsM.urls')),
    path('contact-us/',include('contactUs.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
