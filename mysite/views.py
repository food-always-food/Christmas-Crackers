from django.shortcuts import render
from .apps.christmas import *

# Create your views here.

def home(request):
    return render(request, 'mysite/home.html')

def joke(request):
    response = Joke()
    joke = response['joke']
    answer = response['response']
    request.session['answer'] = answer
    return render(request, 'mysite/joke.html', {"joke":joke,"answer":request.session['answer']})

def trivia(request):
    response = Trivia()
    trivia = response['trivia']
    answer = response['response']
    request.session['answer'] = answer
    return render(request, 'mysite/trivia.html', {"trivia":trivia,"answer":request.session['answer']})

def response(request):
    return render(request, 'mysite/response.html', {"answer":request.session['answer']})
