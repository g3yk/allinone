from django.urls import path

from . import views

urlpatterns = [
    path("update-luggage/<uuid:luggage_id>/", views.LuggageView.as_view()),
]
