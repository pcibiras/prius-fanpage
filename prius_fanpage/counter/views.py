from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ColorFive, ColorTen
from django.forms import modelform_factory

ColorFiveForm = modelform_factory(ColorFive, exclude=[])

@login_required(redirect_field_name='my_redirect_field')
def choose_duration (request):
    # code for a counter form + actual counter should go here
    return render(request, "counter/index.html")
    #the form now works but I still have to add on submit to save to db

@login_required(redirect_field_name='my_redirect_field')  # 5 minute version
def five_min(request):
    form = ColorFiveForm()
    # if request.method == "POST":
    #     form = ColorFiveForm(request.POST)
    #     if form.is_valid():       # TypeError: '<' not supported between instances of 'list' and 'int'
    #         form.save()
    return render(request, "counter/five_min.html", {"form": form})

@login_required(redirect_field_name='my_redirect_field')  # 10 minute version
def ten_min(request):
    return render(request, "counter/ten_min.html")
    # form = ColorForm
    # return render(request, "counter/ten_min.html", {"form": form})


@login_required(redirect_field_name='my_redirect_field')    # generates the result view for 5 min version
def five_min_results(request):
    return render(request, "counter/five_min_results.html")

@login_required(redirect_field_name='my_redirect_field')    # generates the result view for 10 min version
def ten_min_results(request):
    return render(request, "counter/ten_min_results.html")