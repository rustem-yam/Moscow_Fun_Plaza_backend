from django.urls import path
from .views import GetEventView, EventView, CreateEventView

urlpatterns = [
    path('event', EventView.as_view()),
    path('create-event', CreateEventView.as_view()),
    path('get-event', GetEventView.as_view()),
]