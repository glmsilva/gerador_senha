from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/hello.html', {'senha': '123456Gs$', 's': 'senha'})

def password(request):

    senha = list('abcdefghijklmopqrstuvwxyz')
    tamanho = int(request.GET.get('tamanho'))

    if(request.GET.get('numeros')):
        senha.extend('1234567890')   

    if(request.GET.get('maiusculo')):
        senha.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if(request.GET.get('special')):
        senha.extend('@!#$%&()Ç/?><') 

    thepassword = ''
    for x in range(tamanho):
        thepassword += random.choice(senha)



    return render(request, 'generator/password.html', {"password": thepassword})

def about(request):
    return render(request, 'generator/about.html')