from django.shortcuts import render
from .models import User

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


def login (request):
    return render(request, 'login.html')


def control_list ( request ):
    return render ( request, 'control_list.html' )