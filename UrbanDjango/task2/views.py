from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def index_class(request):
    return render(request, 'class_template.html')

def index_func(request):
    return render(request, 'func_template.html')