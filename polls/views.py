from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader

from polls.models import Question


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question DNE")
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    return HttpResponse("TEST")


def vote(request, question_id):
    return HttpResponse("Youre voting on question %s." % question_id)


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
