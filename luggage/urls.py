from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="luggage_index"),
    path("<uuid:luggage_id>", views.details, name="luggage_detail"),
]
