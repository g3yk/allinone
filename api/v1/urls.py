from django.urls import path

from . import views

urlpatterns = [
    path("update-luggage/<int:id>/", views.LuggageView.as_view()),
]
