# from blog.models import Category
from django.shortcuts import render
from django.template import context

# Create your views here.


def index(request):
    # context = {"categories": Category.objects.all()}
    context = {}
    return render(request, "base/index.html", context)
