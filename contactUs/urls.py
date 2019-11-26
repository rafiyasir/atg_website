from django.urls import path

from . import views

urlpatterns = [ 
path('',views.index, name='contactus'),
path('contact',views.contact, name='contactform'),
]