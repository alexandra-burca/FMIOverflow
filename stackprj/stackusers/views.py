from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegisterForm, LoginForm


def registerPage(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"You have created an account with the username {username}. You may login.")
            return redirect('stackbase:home')
    else:
        form = RegisterForm()
    context = {"form": form}
    return render(request, "stackusers/register.html", context)


def loginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            username = form.cleaned_data.get('username')
            user = authenticate(request, username=username, password=password)
            # user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('stackbase:home')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'stackusers/login.html', context)


def profilePage(request):
    return render(request, 'stackusers/profile.html')
