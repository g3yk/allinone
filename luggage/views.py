from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.


def index(request, luggage_id):
    return JsonResponse({"foo": "bar", "id": luggage_id})
