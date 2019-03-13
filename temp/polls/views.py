from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from .models import Choice

from django.template import loader
from django.http import Http404
# Create your views here.
from django.urls import reverse

from django.views import generic

def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:7]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)



class indexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


# class indexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.order_by('-pub_date')[:5]


# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404('Question does not exist')
    
#     return render(request, 'polls/detail.html', {'question' : question})



def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question' : question}) 
    # return HttpResponse('you are requested to question %s.' % question_id)


class detailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

def result(request, question_id):
    response = "you are looking at result of question, %s"
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html',  {'question' : question})

class resultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print("########################################", request.POST['choice'])
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        #selected_choice = question.choice_set.get(request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', {
            'question' : Question,
            'error_message' : 'Choice Does not exist'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    # return HttpResponseRedirect(reverse('polls:results', args=(question.id, )))
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


