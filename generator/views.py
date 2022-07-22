from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html')

def test(request):
    return HttpResponse('<h1>Eggs, are so testy!</h1>') #прямо в коде может применять теги html

def password(request):

    character = list('qwertyuiopasdfghjklzxcvbnm')
    thepassword = ''
    length = int(request.GET.get('length',12))

    if request.GET.get('uppercase'):
        character.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))

    if request.GET.get('numbers'):
        character.extend(list('1234567890'))

    if request.GET.get('special'):
        character.extend(list('!@#$%^&*()_+-='))

    for i in range(length):
        thepassword += random.choice(character)

    return render(request, 'generator/password.html', {'password':thepassword})

def readme(request):
    return render(request, 'generator/readme.html')
