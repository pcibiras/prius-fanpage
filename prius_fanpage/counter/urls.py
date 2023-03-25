from django.urls import path
from . import views

urlpatterns = [
    path('counter/index', views.choose_duration, name='choose_duration'),
    path('counter/five', views.five_min, name='five'),
    path('counter/ten', views.ten_min, name='ten'),
    path('counter/five/results', views.ten_min_results, name='five_min_results'),
    path('counter/ten/results', views.ten_min_results, name='ten_min_results'),
    ]