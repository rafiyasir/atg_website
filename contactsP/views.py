from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactP

def contact(request):
    if request.method == 'POST':
        promo_id = request.POST['promo_id']
        promo = request.POST['promo']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = ContactP.objects.all().filter(promo_id=promo_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquery for this Item')
                return redirect('/promotionals/'+promo_id)

        contact = ContactP(promo=promo, promo_id=promo_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        messages.success(request, 'Your request has been submitted, We will get back to you soon')
        return redirect('/promotionals/'+promo_id)


