from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class index_class(TemplateView):
    template_name = 'class_template.html'

def index_func(request):
    return render(request, 'func_template.html')
