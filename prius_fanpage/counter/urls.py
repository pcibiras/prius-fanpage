from django.urls import path
from . import views

urlpatterns = [
    path('counter/index', views.choose_duration, name='choose_duration'),
    path('counter/five', views.five_min, name='five'),
    path('counter/ten', views.ten_min(), name='ten'),
    ]