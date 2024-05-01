# from blog.models import Category
from django.shortcuts import render
from django.template import context


def index(request):
    context = {}  # {"user": request.user}
    return render(request, "base/index.html", context)
