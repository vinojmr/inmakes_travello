from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import messages
# Create your views here.


def cred(req):
    if req.method == 'POST':
        username = req.POST['username']
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        email = req.POST['email']
        password = req.POST['password']
        pass1 = req.POST['password1']
        if password == pass1:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()
            return render(req, 'travello.html')
    return render(req, 'cred.html')
