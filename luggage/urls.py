from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="luggage_index"),
    path("scanner", views.scanner, name="luggage_scanner"),
    path("<int:luggage_id>", views.details, name="luggage_detail"),
]
