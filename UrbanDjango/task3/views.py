from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


def platform_index(request):
    return render(request, 'platform.html')

class cart_index(TemplateView):
    template_name = 'cart.html'

class games_index(TemplateView):
    template_name = 'games.html'

# def cart_index(request):
#     return render(request, 'cart.html')
#
# def games_index(request):
#     return render(request, 'games.html')