from django.urls import path
from .views import GetEventView, EventView, CreateEventView, GetRecommendEventView

urlpatterns = [
    # path('event', EventView.as_view()),
    # path('create-event', CreateEventView.as_view()),
    path('get-event', GetEventView.as_view()),
    path('get-rec', GetRecommendEventView.as_view()),
]