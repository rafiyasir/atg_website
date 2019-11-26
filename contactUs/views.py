from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactUs

def index(request):
    return render(request, 'contactUs/contact_us.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']


        contact = ContactUs(name=name, email=email, phone=phone, message=message)

        contact.save()

        messages.success(request, 'Thank You For this message, We will get back to you soon')
        return redirect('/contact_us/')


