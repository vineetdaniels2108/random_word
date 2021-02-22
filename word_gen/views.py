from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.

def index(request):
    return HttpResponse("Starting Random Word Generator")


def home(request):
    context = {
        'word' : request.session['word'],
        'counter' : request.session['counter']
    }
    return render (request, 'home.html', context)

def formsubmission(request):
    unique_word = get_random_string()
    request.session['word'] = unique_word
    if 'counter' not in request.session:
        request.session['counter'] = 0
    request.session['counter'] += 1
    return redirect('/home')

def reset(request):
    request.session.flush()
    return redirect('/formsubmission')
    
    
# def display(request): 
#     context = {
#         'word' : request.session['word']
#     }
    
#     return render (request, 'display.html', context)