from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from .models import List


# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"
    # Here we are adding a method that will be ran when we are dealing with a GET request
    # def get(self, request):
    #     # Here we are returning a generic response
    #     # This is similar to response.send() in express
    #     return HttpResponse("Home")

class Lists(TemplateView):
    template_name = "lists_list.html"

def lists_index(request):
    lists = List.objects.all()
    return render(request, 'lists_list.html', { 'lists': lists })