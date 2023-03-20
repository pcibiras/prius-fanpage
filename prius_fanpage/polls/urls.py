from django.urls import path

from . import views

urlpatterns = [
    path('polls/<int:question_id>/results/', views.results, name='results'),
    path('polls/<int:question_id>/vote/', views.vote, name='vote'),
    ]