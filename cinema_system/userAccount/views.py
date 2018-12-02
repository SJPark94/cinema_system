from django.shortcuts import render, redirect
from .forms import UserRegister
from django.core.mail import send_mail
import string, random
from .models import UserInfo
# Create your views here.


def homepage(request):
    return render(request, 'homepage/index.html')

def registerRequest(request):
    if request.method == 'POST':
        user = UserRegister(request.POST)
        if user.is_valid():
            email = user.clean_email()
            firstname = user.getFirstName()
            lastname = user.getLastName()
            user.save()
            code = codeGenerator(email)
            sendEmail(request, email, firstname, lastname, code)
            request.session['email'] = email
            print(request.session['email'])
            #return render(request, 'registration/register_email_sent.html', {'user': user})
            return redirect('http://127.0.0.1:8000/accounts/activation/')
    else:
        user = UserRegister()
    return render(request, 'registration/register.html', {'register': user})

def sendEmail(request, email, firstname, lastname, code):
    user = UserRegister(request.POST)
    subject = 'Hello from Cinema E-Booking System!'
    body = 'Welcome, ' + firstname + ' ' + lastname + ". We have the best online ticketing system in the world. \nPlease use this code " + code + " to finish activating your account!"
    botEmail = 'sunnybot94@gmail.com'
    send_mail(subject, body, botEmail, [email], fail_silently=False)
    return render(request, 'registration/register_email_sent.html', {'user': user})

def codeGenerator(email):
    code = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))
    user = UserInfo.objects.get(email=email)
    user.activation_code = code
    user.save()
    return code

def activateAccount(request):
    if request.method == 'POST':
        email = request.session['email']
        user = UserInfo.objects.get(email=email)
        code = request.POST.get('code')
        if(user.activation_code == code):

            user.email_confirmed = True
            user.active = True;
            user.save()
            return render(request, 'registration/account_activation_confirmed.html')
        else:
            return render(request, 'registration/register_email_sent.html')
    return render(request, 'registration/register_email_sent.html')

def viewProfile(request):
    user = request.user
    return render(request, 'profile/view_profile.html', {'user': user})