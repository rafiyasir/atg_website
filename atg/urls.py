
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
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
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
