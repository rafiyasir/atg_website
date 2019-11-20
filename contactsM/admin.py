from django.contrib import admin

from .models import ContactM

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'misc', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'misc')
    list_per_page = 25

admin.site.register(ContactM, ContactAdmin)
