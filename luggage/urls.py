from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="luggage_index"),
    path("scanner1", views.scanner1, name="luggage_scanner"),
    path("scanner2", views.scanner2, name="luggage_scanner"),
    path("scanner3", views.scanner3, name="luggage_scanner"),
    path("scanner4", views.scanner4, name="luggage_scanner"),
    path("<int:luggage_id>", views.details, name="luggage_detail"),
]
