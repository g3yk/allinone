from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Luggage
from django.shortcuts import redirect


def index(request):
    user = request.user
    if user.is_authenticated:
        luggages = Luggage.objects.filter(passenger=user)
        status = {}
        message = {}
        states = [ "Check−in has been completed, and waiting for baggage...",
                    "Your baggage has been put on the conveyor belt.",
                    "Your baggage about to be loaded onto the plane.",
                    "Your baggage has successfully put to the plane.",
                    "Your baggage has been delivered" ]

        for luggage in luggages:
            state = 0

            if luggage.status1:
                state = 1
            if luggage.status2:
                state = 2
            if luggage.status3:
                state = 3
            if luggage.status4:
                state = 4

            x = {}
            for i in range(state, 5):
                x[i] = "deactive"
            
            x[state] = "active"
            status[luggage.pk] = x
            message[luggage.pk] = states[state]

        return render(request, "luggage/index.html", {"luggages": luggages, "status": status, "message": message})
    else:
        return redirect("login")


def details(request, luggage_id):
    user = request.user
    if user.is_authenticated:
        luggage = Luggage.objects.filter(
            passenger=user).filter(id=luggage_id)
        return render(request, "luggage/details.html", {"luggage": luggage.first()})
    else:
        return redirect("home")


def scanner1(request):
    return render(request, "luggage/scanner1.html")

def scanner2(request):
    return render(request, "luggage/scanner2.html")
def scanner3(request):
    return render(request, "luggage/scanner3.html")
def scanner4(request):
    return render(request, "luggage/scanner4.html")