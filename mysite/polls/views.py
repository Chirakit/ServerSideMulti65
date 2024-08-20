from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "index.html", context)

def detail(request, question_id):
    q = Question.objects.get(id=question_id)
    context = {
        "q": q
    }
    return render(request, "detail.html", context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id, choice_id):
    c = Choice.objects.get(id=choice_id, question_id=question_id)
    c.votes += 1
    c.save()
    return HttpResponse("You're voting on question %s." % question_id)
