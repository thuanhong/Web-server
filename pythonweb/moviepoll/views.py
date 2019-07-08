from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Question, Choice
from django.utils import timezone

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        temp_dict = {
            'question': question,
            'error_message': "You didn't select a choice."
        }
        return render(request, 'detail.html', temp_dict)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))

def home(request):
    my_dict = {'content':'Home Page'}
    return render(request, 'home.html', context=my_dict)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    total = 0
    for choice in question.choice_set.all():
        total += choice.votes
    my_dict = {
        'question':question,
        'value':total,
    }
    return render(request, 'results.html', my_dict)