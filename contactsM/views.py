from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactM

def contact(request):
    if request.method == 'POST':
        misc_id = request.POST['misc_id']
        misc = request.POST['misc']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = ContactM.objects.all().filter(misc_id=misc_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquery for this Item')
                return redirect('/miscellaneous/'+misc_id)

        contact = ContactM(misc=misc, misc_id=misc_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        messages.success(request, 'Your request has been submitted, We will get back to you soon')
        return redirect('/miscellaneous/'+misc_id)


