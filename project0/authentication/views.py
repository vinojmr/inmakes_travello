from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from app0.models import Travel, Team


# Create your views here.

def html(req):
    return render(req, 'html.html')


def login(request):
    obj = Travel.objects.all()
    obj1 = Team.objects.all()
    if request.method == 'POST':

        username1 = request.POST['username']
        password1 = request.POST['password']
        users = auth.authenticate(username=username1, password=password1)
        if users is None:
            messages.info(request, 'invalid credentials')
        else:
            return render(request, 'travello.html', {'user': users, 'result': obj, 'team': obj1})
    return render(request, 'login.html',)


def log(request):
    if request.method == 'POST':
        user = request.POST['user_name']
        pas = request.POST['password']
        first = request.POST['first_name']
        email = request.POST['email']
        last = request.POST['last_name']
        pass1 = request.POST['password1']
        if pas == pass1:
            if User.objects.filter(username=user).exists():
                messages.info(request, 'Username already taken, use another name')
                return redirect('log')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'account with this email already exists, login')
                return redirect('log')
            else:
                users = User.objects.create_user(username=user, password=pas, first_name=first, last_name=last,
                                                 email=email)
                users.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords dont match')
            return redirect('log')
        return redirect('/')
    return render(request, 'cred.html')


def logout(req):
    auth.logout(req)
    return redirect('/')
