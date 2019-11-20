from django.contrib import admin

from .models import ContactP

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'promo', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'promo')
    list_per_page = 25

admin.site.register(ContactP, ContactAdmin)
