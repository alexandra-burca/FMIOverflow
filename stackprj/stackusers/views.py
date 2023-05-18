from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def register(request):
    form = UserCreationForm()
    context = {"form" : form }
    return render(request,"stackusers/register.html",context)


def login(request):
    return render(request,"login.html")