from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
import matplotlib.pyplot as plt
import io
import urllib
import base64

def vote(request):

    question = Question.objects.get(id=1)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):     # if user has not checked a field - an exception is raised
        return render (request, 'website/home.html', {
            'question': question,
            'error_message': "You didn't select a choice.",     # error message to be displayed in the html form
        })
    else:
        selected_choice.votes += 1      # appends to 'votes' in 'choices' the db table
        selected_choice.save()      # saves the result to the db
        # here should be a line that checks if the user has already voted. User model should be made custom. Also html form should be changed with an if statement.
        return HttpResponseRedirect(reverse('results'))     # this line makes sure the result is not posted to the db if user refreshed the page

def results(request):
    question = Question.objects.get(id=1)

    # code for the plot
    x = [choice.choice_text for choice in Choice.objects.all()]     # list comprehention to parse db data
    y = [choice.votes for choice in Choice.objects.all()]       # list comprehention to parse db data
    plt.bar(x, y, color="#850000")
    plt.title("Votes")
    plt.ylabel("Nr. of votes")
    plt.xticks(rotation=15)     # rotates bar labels
    plt.tight_layout()     # this function keeps the plot from being cut off
    fig = plt.gcf()     # gcf - get current figure
    buf = io.BytesIO()      # lines below converts the plot to a html friendly format
    fig.savefig(buf)
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request, "polls/results.html", {"question":question, "data":uri})

