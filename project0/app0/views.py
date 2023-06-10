from django.shortcuts import render
from django.http import HttpResponse
from .  models import Travel, Team
# Create your views here.


def demo(request):
    return render(request, 'add.html')


def about(request):
    return render(request, 'about.html')


def contact():
    return HttpResponse('<h4>8590221689</h4>')


def add(req):
    a = int(req.GET['num1'])
    b = int(req.GET['num2'])
    res = a+b
    return render(req, 'result.html', {'result': res})


def static(req):
    obj = Travel.objects.all()
    obj1 = Team.objects.all()
    return render(req, 'travello.html', {'result': obj, 'team': obj1})

def templates(req):
    return render(req, 'cred.html')