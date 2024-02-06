from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def login_view(request: HttpRequest):
    if request.method == "GET":
        if request.user.is_authentificated:
            return redirect('')
        return render(request, 'authentification/login.html')

    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(request, username=username, password=password)
    if user is not None:
        return redirect('')
    return render(request, "authentification/login.html", {"error": "Invalid login forms"})