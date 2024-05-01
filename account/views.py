from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.http import HttpResponse
# Create your views here.


def login_request(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            if "@" in username:
                user = User.objects.get(email=username)
            else:
                user = User.objects.get(username=username)

            auth = user.check_password(password)
        except User.DoesNotExist:
            auth = False

        if auth:
            login(request, user)  # type: ignore
            return redirect("home")

        else:
            return render(request, "account/login.html", {
                "error": "username or password is not valid"
            })

    return render(request, "account/login.html")


def register_request(request):

    if request.user.is_authenticated:
        return redirect("home")

    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["first_name"]
        lastname = request.POST["last_name"]
        password = request.POST["password1"]

        user = User.objects.create_user(username=username, email=email,
                                        first_name=firstname, last_name=lastname, password=password)
        user.save()
        return redirect("login")

    return render(request, "account/register.html", {"form": form})


def logout_request(request):
    logout(request)
    return redirect("home")
