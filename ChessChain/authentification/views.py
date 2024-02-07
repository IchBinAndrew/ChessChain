from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm

# Create your views here.

def login_view(request: HttpRequest):
    if request.method == "GET":
        return render(request, 'authentification/login.html')
    form = LoginForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        user = authenticate(request, username=cd['username'], password=cd['password'])
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, "authentification/login.html", {"error": "Invalid login forms"})


def register_view(request: HttpRequest):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'authentification/signup.html', {'form': form})


def logout_view(request: HttpRequest):
    logout(request)
    return render(request, 'authentification/logout.html')