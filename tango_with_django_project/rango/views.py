from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    
    context_dict = {'boldmessage': 'Welcome to Rango, pardner!'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'about_message': 'We are like burrito cats!'}
    return render(request, 'rango/about.html', context=context_dict)