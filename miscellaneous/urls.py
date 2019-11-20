from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='misc_items'),
    path('<int:miscellaneous_id>', views.miscellaneous, name='misc_item'),
]