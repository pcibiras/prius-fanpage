from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def welcome(request):
    return render(request, "website/home.html")


@login_required(redirect_field_name='my_redirect_field')
def jokes (request):
    return render(request, "website/jokes.html")

@login_required(redirect_field_name='my_redirect_field')
def counter (request):
    # code for a counter form + actual counter should go here
    return render(request, "website/counter.html")