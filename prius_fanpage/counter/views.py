from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Color
from django.forms import modelform_factory

ColorForm = modelform_factory(Color, exclude=[])

@login_required(redirect_field_name='my_redirect_field')
def choose_duration (request):
    # code for a counter form + actual counter should go here
    form = ColorForm
    return render(request, "counter/index.html", {"form": form})
    #the form now works but I still have to add on submit to save to db

@login_required(redirect_field_name='my_redirect_field')
def five_min():
    pass

@login_required(redirect_field_name='my_redirect_field')
def ten_min():
    pass