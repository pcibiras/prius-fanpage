from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import ColorFive, ColorTen
from .forms import CountFiveForm, CountTenForm
from .models import CountFive, CountTen
from django.forms import modelform_factory

ColorFiveForm = modelform_factory(ColorFive, exclude=[])

@login_required(redirect_field_name='my_redirect_field')
def choose_duration (request):
    # code for a counter form + actual counter should go here
    return render(request, "counter/index.html")
    #the form now works but I still have to add on submit to save to db

@login_required(redirect_field_name='my_redirect_field')  # 5 minute version
def five_min(request):
    if request.method == "POST":
        form = CountFiveForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('five_min_results'))
    else:
        form = CountFiveForm()
    return render(request, 'counter/five_min.html', {'form': form})


    # form = ColorFiveForm()
    # if request.method == "POST":
    #     form = ColorFiveForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    # return render(request, "counter/five_min.html", {"form": form})

@login_required(redirect_field_name='my_redirect_field')  # 10 minute version
def ten_min(request):
    if request.method == "POST":
        form = CountTenForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ten_min_results'))
    else:
        form = CountTenForm()
    return render(request, 'counter/ten_min.html', {'form': form})

@login_required(redirect_field_name='my_redirect_field')    # generates the result view for 5 min version
def five_min_results(request):
    # gets the average for five min version
    all_numbers = [number.number for number in CountFive.objects.all()]
    five_average = round(sum(all_numbers) / len(all_numbers))
    # gets the latest instance in db to display users score
    obj = CountFive.objects.order_by('-id')[0]
    user_score = obj.number
    return render(request, "counter/five_min_results.html", {"average": five_average, "user_score": user_score})

@login_required(redirect_field_name='my_redirect_field')    # generates the result view for 10 min version
def ten_min_results(request):
    # gets the average for ten min version
    all_numbers = [number.number for number in CountTen.objects.all()]
    ten_average = round(sum(all_numbers) / len(all_numbers))
    # gets the latest instance in db to display users score
    obj = CountTen.objects.order_by('-id')[0]
    user_score = obj.number
    return render(request, "counter/ten_min_results.html", {"average": ten_average, "user_score": user_score})
