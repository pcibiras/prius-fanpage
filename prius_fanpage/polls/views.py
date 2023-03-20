from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse

def vote(request):

    question = Question.objects.get(id=1)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render (request, 'website/home.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results'))
def results(request):
    return render(request, "polls/results.html")

