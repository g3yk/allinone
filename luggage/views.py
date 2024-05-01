from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Luggage
from django.shortcuts import redirect


def index(request):
    user = request.user
    if user.is_authenticated:
        luggages = Luggage.objects.filter(passenger=user)
        return render(request, "luggage/index.html", {"luggages": luggages})
    else:
        return redirect("home")


def details(request, luggage_id):
    user = request.user
    if user.is_authenticated:
        luggage = Luggage.objects.filter(
            passenger=user).filter(id=luggage_id)
        return render(request, "luggage/details.html", {"luggage": luggage.first()})
    else:
        return redirect("home")


def scanner(request):
    return render(request, "luggage/scanner.html")
