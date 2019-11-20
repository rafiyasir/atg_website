from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contact(request):
    if request.method == 'POST':
        bag_id = request.POST['bag_id']
        bag = request.POST['bag']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(bag_id=bag_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquery for this bag')
                return redirect('/bags/'+bag_id)

        contact = Contact(bag=bag, bag_id=bag_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        messages.success(request, 'Your request has been submitted, We will get back to you soon')
        return redirect('/bags/'+bag_id)


