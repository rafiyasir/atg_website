from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='promotionals'),
    path('<int:promotional_id>', views.promotional, name='promotional'),
]