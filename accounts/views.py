from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from contactsM.models import ContactM
from contactsP.models import ContactP

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=name)
                    #login after register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now Logged in')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'You are now registerd and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now Logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now Logged out')
        return redirect('index')
    

def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    user_contactsm = ContactM.objects.order_by('-contact_date').filter(user_id=request.user.id)
    user_contactsp = ContactP.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contacts,
        'contactsm' : user_contactsm,
        'contactsp' : user_contactsp
    }
    return render(request,'accounts/dashboard.html', context)
