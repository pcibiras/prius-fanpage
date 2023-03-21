from django.shortcuts import render
from django.contrib.auth.decorators import login_required



@login_required(redirect_field_name='my_redirect_field')
def counter (request):
    # code for a counter form + actual counter should go here
    return render(request, "counter/counter.html")