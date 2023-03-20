from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from polls.models import Question, Choice



def welcome(request):
    questions = Question.objects.all()
    return render(request, "website/home.html", {"questions":questions})

@login_required(redirect_field_name='my_redirect_field')
def jokes (request):
    return render(request, "website/jokes.html")

@login_required(redirect_field_name='my_redirect_field')
def counter (request):
    # code for a counter form + actual counter should go here
    return render(request, "website/counter.html")