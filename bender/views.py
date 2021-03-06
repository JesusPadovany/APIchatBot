from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from bender.models import Question, Answer, Product, Member
from bender.models import Member as MemberModel
from bender.models import Benefit as BenefitModel
from bender.serializers import QuestionSerializer,AnswerSerializer
import random
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, TemplateView

class Indice(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        products = Product.objects.all()
        members = MemberModel.objects.all()
        benefits = BenefitModel.objects.all()
        context = { 'products' : products,
                    'members' : members,
                    'benefits' : benefits
                  }
        return context

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def question_list(request):
    """
    List all code question, or create a new question.
    """
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def answer_list(request):
    """
    List all code answer, or create a new answer.
    """
    if request.method == 'GET':
        answers = Answer.objects.all()
        serializer = AnswerSerializer(answers, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AnswerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def question_detail(request, pk):
    """
    Retrieve, update or delete a Question.
    """
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = QuestionSerializer(question, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        question.delete()
        return HttpResponse(status=204)

@csrf_exempt
def answer_detail(request, pk):
    """
    Retrieve, update or delete a Answer.
    """
    try:
        answer = Answer.objects.get(pk=pk)
    except Answer.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AnswerSerializer(answer)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AnswerSerializer(answer, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        answer.delete()
        return HttpResponse(status=204)

@csrf_exempt
def bot(request, str):
    if request.method == 'GET':
        sch = search(str)
        if sch == "No encontrada":
            question = Question.objects.filter(question_text='Desconocida').values('id')
        else:
            question = Question.objects.filter(question_text__startswith=sch).values('id')
        answer = random.choice(Answer.objects.filter(question__id__in=question))
        serializer = AnswerSerializer(answer)
        return JSONResponse(serializer.data)

def search_keywords(str):
	keywords = ["donde", "como", "cuando", "me duele", "que", "remedios para", "hola", "buenas", "adios",
                "gracias", "medios"]
	x = str.lower()
	pos = -1
	for kw in keywords:
		pos = x.find(kw)
		if pos >= 0: break
	return pos

def search(str):
    pos = search_keywords(str)
    if pos >= 0:
        return str[pos:len(str)]
    else:
        return "No encontrada"


