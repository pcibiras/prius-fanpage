from django.urls import path

from . import views

urlpatterns = [
    path('polls/results', views.results, name='results'),
    path('polls/vote', views.vote, name='vote'),
    ]