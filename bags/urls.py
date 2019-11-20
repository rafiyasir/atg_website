from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='bags'),
    path('<int:bag_id>', views.bag, name='bag'),
]