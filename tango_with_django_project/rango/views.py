from django.shortcuts import render
from django.http import HttpResponse
from rango import models

def about(request):
    context_dict = {'about_message': 'We are like burrito cats!'}
    return render(request, 'rango/about.html', context=context_dict)

def index(request):
    category_list = models.Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = models.Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category

    except models.Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None

    return render(request, 'rango/category.html', context_dict)
